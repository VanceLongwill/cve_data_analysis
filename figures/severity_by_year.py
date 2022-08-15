import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def relative_freqs(x):
    severities = ['CRITICAL', 'HIGH',  'LOW',  'MEDIUM', 'None']
    values = [x[sv] for sv in severities]
    s = np.nansum(values)
    return [v/s for v in values]


def severity_by_year(df: pd.DataFrame):
    grouped = df.groupby(['Year', 'SEVERITY'], dropna=False).sum()
    print(grouped)

    print(grouped.head(20))
    # print(grouped.head(20).value_counts(normalize=True))

    pivoted = grouped.pivot_table('index', ['Year'], 'SEVERITY')

    print(pivoted.head(20))

    # pivoted = pivoted.replace(np.NaN, 0)
    #pivoted['Relative freq MEDIUM'] = pivoted[severities].sum(axis=1)

    pivoted = pivoted.fillna(0)
    pivoted = pivoted.apply(relative_freqs, axis=1, result_type='broadcast')
    print(pivoted.head(20))

    #lp = sns.countplot(data=pivoted)
    #lp.set_title("Severity by year")
    b = pivoted.plot.bar()
    plt.show()
