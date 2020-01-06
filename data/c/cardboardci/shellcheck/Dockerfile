FROM koalaman/shellcheck:v0.7.0 AS official
FROM alpine:3.10.3
COPY --from=official /bin/shellcheck /bin/shellcheck

##
## Image Metadata
##
ARG build_date
ARG version
ARG vcs_ref
LABEL maintainer = "CardboardCI" \
    \
    org.label-schema.schema-version = "1.0" \
    \
    org.label-schema.name = "shellcheck" \
    org.label-schema.version = "${version}" \
    org.label-schema.build-date = "${build_date}" \
    org.label-schema.release= = "CardboardCI version:${version} build-date:${build_date}" \
    org.label-schema.vendor = "cardboardci" \
    org.label-schema.architecture = "amd64" \
    \
    org.label-schema.summary = "Shell script static anaylsis" \
    org.label-schema.description = "ShellCheck is a static anaylsis tool that automatically finds bugs in your shell scripts" \
    \
    org.label-schema.url = "https://gitlab.com/cardboardci/images/shellcheck" \
    org.label-schema.changelog-url = "https://gitlab.com/cardboardci/images/shellcheck/releases" \
    org.label-schema.authoritative-source-url = "https://cloud.docker.com/u/cardboardci/repository/docker/cardboardci/shellcheck" \
    org.label-schema.distribution-scope = "public" \
    org.label-schema.vcs-type = "git" \
    org.label-schema.vcs-url = "https://gitlab.com/cardboardci/images/shellcheck" \
    org.label-schema.vcs-ref = "${vcs_ref}" \
