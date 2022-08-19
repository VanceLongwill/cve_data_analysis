from cve import software_development

from figures import vulnerability_type, cwe_severity, severity_by_year

sd = software_development()

datasets = [sd]

for df in datasets:
    vulnerability_type.vulnerability_types_by_year(df)
    vulnerability_type.dispersion_of_vulnerability_types_by_year(df)
    vulnerability_type.correlation_of_vulnerability_type_dispersion_and_count(df)
    vulnerability_type.vulnerability_types_year_introduced(df)
    vulnerability_type.vulnerability_types_year_introduced_cumulative(df)
    cwe_severity.yoy_mean_cvss_score_vs_count(df)
    cwe_severity.box(df)
    cwe_severity.distributions_per_year(df)
    cwe_severity.hist(df)
    cwe_severity.top10s(df)
    severity_by_year.severity_by_year(df)
