import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def top_vulns(df: pd.DataFrame):
    top10 = df['CWE-NAME'].value_counts(normalize=True).head(10)
    return top10


def remove_non_numerical_scores(df: pd.DataFrame, numerical_types=[int, np.int64, float, np.float64]) -> pd.DataFrame:
    return df[df['CVSS-V2'].apply(lambda x: type(x) in numerical_types)]


def aggregate_mean_scores_and_counts(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby(['CWE-ID', 'CWE-NAME'])

    stats = grouped.agg({'CVSS-V2': 'mean', 'CWE-NAME': 'count'})

    stats = stats.rename(
        columns={'CVSS-V2': 'Mean CVSS-V2 score', 'CWE-NAME': 'Count'}
    )

    return stats


def yoy_mean_cvss_score_vs_count(df: pd.DataFrame):
    sanitized = remove_non_numerical_scores(df)

    grouped = sanitized.groupby('Year')

    stats = grouped.agg(Mean=('CVSS-V2', np.mean),
                        Count=pd.NamedAgg(column='Year', aggfunc='count'))

    stats = stats.rename(
        columns={'Mean': 'Mean CVSS-V2 score',
                 'Count': 'Number of vulnerabilities disclosed'}
    )
    ax = stats.plot(kind='line', y='Mean CVSS-V2 score', ylim=(0, 10),
                    ylabel="Mean CVSS-V2 score", color="red")

    ax1 = ax.twinx()
    stats.plot(kind='line', y='Number of vulnerabilities disclosed', ax=ax1, ylim=(0, 10000),
               ylabel="Number of vulnerabilities disclosed",
               title="Year on year: the mean CVSS-V2 scores of all vulnerabilities vs the total number of vulnerabilities")

    plt.show()


def distributions_per_year(df: pd.DataFrame):
    sanitized = remove_non_numerical_scores(df)

    grouped = sanitized
    stats = grouped.agg(Count=pd.NamedAgg(
        column='CVSS-V2', aggfunc='value_counts'))
    print(stats)
    stats = stats.groupby('Year')

    stats.plot(kind='line', y='Count', x='CVSS-V2')
    plt.show()


def box(df: pd.DataFrame):
    sanitized = remove_non_numerical_scores(df)
    stats = aggregate_mean_scores_and_counts(sanitized)
    stats.plot(kind='box', column='Mean CVSS-V2 score')
    plt.show()


def top10s(df: pd.DataFrame):
    sanitized = remove_non_numerical_scores(df)
    stats = aggregate_mean_scores_and_counts(sanitized)

    top10_most_severe = stats.nlargest(10, columns=['Mean CVSS-V2 score']).round(2)
    print("Most severe")
    print(top10_most_severe.to_csv())
    print("")

    top10_most_common = stats.nlargest(10, columns=['Count']).round(2)
    print("Most common")
    print(top10_most_common.to_csv())
    print("")

    # 10 most severe from the 50 most common
    top10_most_impactful = stats.nlargest(50, columns=['Count']).nlargest(
        10, columns=['Mean CVSS-V2 score']).round(2)
    print("Most impactful")
    print(top10_most_impactful.to_csv())
    print("")


def hist(df: pd.DataFrame):
    sanitized = remove_non_numerical_scores(df)
    binwidth = 2

    ax = sanitized['CVSS-V2'].plot(
        kind='hist',
        xlim=(0, 10),
        title='Histogram of CVSS-V2 scores of vulnerabilities',
        xlabel='CVSS-V2 score',
        ylabel='Frequency',
        bins=range(0, 10 + binwidth, binwidth)
    )

    # show bar height annotation
    ax.bar_label(ax.containers[0])

    plt.show()


def scatter(df: pd.DataFrame):
    sanitized = remove_non_numerical_scores(df)
    stats = aggregate_mean_scores_and_counts(sanitized)

    top10_most_severe = stats.nlargest(10, columns=['Mean CVSS-V2 score'])
    print(top10_most_severe)

    # stats.plot(kind='box', x='Count', y='Mean CVSS-V2 score')
    # stats.plot(kind='scatter', x='Count', y='Mean CVSS-V2 score')
    stats.plot(kind='line')
    plt.show()
