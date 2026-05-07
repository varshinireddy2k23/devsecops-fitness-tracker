package devsecops

default allow = true

deny[msg] {
    input.Results[_].Vulnerabilities[_].Severity == "CRITICAL"
    vuln := input.Results[_].Vulnerabilities[_]
    msg := sprintf("BLOCKED: CRITICAL vulnerability found: %s", [vuln.VulnerabilityID])
}

deny[msg] {
    vuln := input.Results[_].Vulnerabilities[_]
    vuln.Severity == "HIGH"
    not vuln.FixedVersion
    msg := sprintf("BLOCKED: HIGH vulnerability without fix: %s", [vuln.VulnerabilityID])
}
