ARG BASE=latest
FROM hadolint/hadolint:${BASE} AS source 

FROM alpine:latest AS distro
COPY --from=source /bin/hadolint /bin/hadolint
