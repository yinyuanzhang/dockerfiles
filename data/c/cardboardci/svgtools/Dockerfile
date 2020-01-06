FROM alpine:3.8
RUN apk add --no-cache librsvg=2.40.20-r0

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
    org.label-schema.name = "svgtools" \
    org.label-schema.version = "${version}" \
    org.label-schema.build-date = "${build_date}" \
    org.label-schema.release= = "CardboardCI version:${version} build-date:${build_date}" \
    org.label-schema.vendor = "cardboardci" \
    org.label-schema.architecture = "amd64" \
    \
    org.label-schema.summary = "Rasterize SVGs" \
    org.label-schema.description = "Tools for working with Scalable Vector Graphics (SVG) files" \
    \
    org.label-schema.url = "https://gitlab.com/cardboardci/images/svgtools" \
    org.label-schema.changelog-url = "https://gitlab.com/cardboardci/images/svgtools/releases" \
    org.label-schema.authoritative-source-url = "https://cloud.docker.com/u/cardboardci/repository/docker/cardboardci/svgtools" \
    org.label-schema.distribution-scope = "public" \
    org.label-schema.vcs-type = "git" \
    org.label-schema.vcs-url = "https://gitlab.com/cardboardci/images/svgtools" \
    org.label-schema.vcs-ref = "${vcs_ref}" \