import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

severities = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'None']


def relative_freqs(x):
    values = []
    for sv in severities:
        if sv in x:
            values.append(x[sv])
    s = np.nansum(values)
    return [v/s for v in values]

def severity_by_year(df: pd.DataFrame):
    grouped = df.groupby(['Year', 'SEVERITY'], dropna=False).sum()
    # pivot the data to have each severity as a column
    pivoted = grouped.pivot_table('index', ['Year'], 'SEVERITY')
    # build a list of the severity labels present to avoid throwing a KeyError
    severities_present = [sv for sv in severities if sv in pivoted.columns]
    pivoted = pivoted.loc[:, severities_present]
    # replace NaN with zero
    pivoted = pivoted.fillna(0)
    # calculate the relative frequencies of each severity in each row (year)
    pivoted = pivoted.apply(relative_freqs, axis=1, result_type='broadcast')
    # grab the latest 10 years of data
    last_10_years = pivoted

    # plot as bar graph
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
