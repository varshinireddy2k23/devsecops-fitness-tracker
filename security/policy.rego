package kubernetes.security

deny contains msg if {
    input.kind == "Deployment"
    not input.spec.template.spec.securityContext.runAsNonRoot

    msg := "Container must not run as root"
}

deny contains msg if {
    input.kind == "Deployment"

    container := input.spec.template.spec.containers[_]
    not container.resources.limits

    msg := "Container must have resource limits"
}