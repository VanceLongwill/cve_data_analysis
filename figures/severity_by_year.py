import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

severities = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'None']

def relative_freqs(x):
    values = [x[sv] for sv in severities]
    s = np.nansum(values)
    return [v/s for v in values]


def severity_by_year(df: pd.DataFrame):
    grouped = df.groupby(['Year', 'SEVERITY'], dropna=False).sum()
    pivoted = grouped.pivot_table('index', ['Year'], 'SEVERITY')
    pivoted = pivoted.loc[:, severities]
    pivoted = pivoted.fillna(0)
    pivoted = pivoted.apply(relative_freqs, axis=1, result_type='broadcast')
    last_10_years = pivoted.tail(10)

    bg = last_10_years.plot(kind='bar', color={
        'CRITICAL': '#780000',
        'HIGH': '#dc0000',
        'MEDIUM': '#fd8c00',
        'LOW': '#fdc500',
        'None': 'grey',
    })

    # format decimal as percentage
    bg.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    plt.title(
        'Relative frequencies of the severity levels of vulnerabilities by year')
    plt.ylabel('Relative frequency (percentage)')
    plt.xlabel('Year')
    plt.show()
