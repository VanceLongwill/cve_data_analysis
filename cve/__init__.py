import pandas as pd


def year_from_cve_id(cve_id):
    return cve_id.split("-")[1]


def load_sheet(fn):
    df = pd.read_excel(fn, sheet_name=0)

    year_list = []
    for i in range(0, len(df["CVE-ID"])):
        # CVE-1999-0199
        a = year_from_cve_id(df["CVE-ID"][i])
        year_list.append(a)

    df.insert(loc=2, column='Year', value=year_list)

    # only include years 2002 - 2020 inclusive
    df = df.loc[(df['Year'] > '2001') & (df['Year'] < '2021')]

    return df


def software_development():
    fn = "./archive/Software Development/SD_Vulnerability_Dataset.xlsx"
    return load_sheet(fn)


#Not used
#def hardware_design():
#    fn = "./archive/Hardware Design/HD_Vulnerability_Dataset.xlsx"
#    return load_sheet(fn)
#
#
#def research_concept():
#    fn = "./archive/Research Concept/RC_Vulnerability_Dataset.xlsx"
#    return load_sheet(fn)
