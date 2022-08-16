import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np


def top_vulns(df: pd.DataFrame):
    top10 = df['CWE-NAME'].value_counts(normalize=True).head(10)
    return top10


def remove_non_numerical_scores(df: pd.DataFrame) -> pd.DataFrame:
    numerical_types = [int, np.int64, float, np.float64]
    return df[df['CVSS-V2'].apply(lambda x: type(x) in numerical_types)]


def aggregate_mean_scores(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby('CWE-NAME')

    stats = grouped.agg({'CVSS-V2': 'mean', 'CWE-NAME': 'count'})

    stats = stats.rename(
        columns={'CVSS-V2': 'Mean CVSS-V2 score', 'CWE-NAME': 'Count'}
    )

    return stats


def scatter(df: pd.DataFrame):
    sanitized = df[df['CVSS-V2'].apply(lambda x: type(x)
                                       in [int, np.int64, float, np.float64])]

    grouped = sanitized.groupby('CWE-NAME')

    stats = grouped.agg({'CVSS-V2': 'mean', 'CWE-NAME': 'count'}).rename(
        columns={'CVSS-V2': 'Mean CVSS-V2 score', 'CWE-NAME': 'Count'})

    top10_most_severe = stats.nlargest(10, columns={'Mean CVSS-V2 score'})
    print(top10_most_severe)

    stats.plot(kind='box', x='Count', y='Mean CVSS-V2 score')
    stats.plot(kind='scatter', x='Count', y='Mean CVSS-V2 score')
    plt.show()
