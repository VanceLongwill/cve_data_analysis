import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def vulnerabilities_by_year(df):
    plt.rcParams["figure.figsize"] = (20, 10)
    sns.set_theme(style="darkgrid")

    ax = sns.countplot(x="Year", data=df, palette="hls")
    ax.set_title("Vulnerabilities By Year")
    for p in ax.patches:
        ax.annotate('{:.0f}'.format(p.get_height()),
                    (p.get_x()+0.1, p.get_height()+50))
    plt.xticks(rotation=90)
    plt.show()
