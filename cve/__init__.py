import pandas as pd

fn = "./archive/Software Development/SD_Vulnerability_Dataset.xlsx"
df = pd.read_excel(fn, sheet_name=0)

def year_from_cve_id(cve_id):
    return cve_id.split("-")[1]


year_list = []
for i in range(0, len(df["CVE-ID"])):
    # CVE-1999-0199
    a = year_from_cve_id(df["CVE-ID"][i])
    year_list.append(a)

df.insert(loc=2, column='Year', value=year_list)
