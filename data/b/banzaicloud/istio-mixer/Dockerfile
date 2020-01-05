# BASE_DISTRIBUTION is used to switch between the old base distribution and distroless base images
ARG BASE_DISTRIBUTION=distroless

ARG GO_VERSION=1.13

FROM golang:${GO_VERSION}-alpine AS builder

RUN mkdir -p /go/src/istio.io/istio
WORKDIR /go/src/istio.io/istio

ENV ISTIO_ENVOY_LINUX_DEBUG_PATH /bin/false
ENV ISTIO_ENVOY_LINUX_RELEASE_PATH /bin/false

COPY . ./

RUN apk --no-cache add bash=5.0.0-r0 make=4.2.1-r2 git=2.22.0-r0 ca-certificates=20190108-r0 curl=7.66.0-r0

RUN make build


# The following section is used as base image if BASE_DISTRIBUTION=default
# No tag available https://hub.docker.com/_/scratch?tab=description
# hadolint ignore=DL3006
FROM scratch as default
# The following section is used as base image if BASE_DISTRIBUTION=distroless
# hadolint ignore=DL3007
FROM gcr.io/distroless/static:latest as distroless

# This will build the final image based on either default or distroless from above
# hadolint ignore=DL3006
FROM ${BASE_DISTRIBUTION}

COPY --from=builder /go/src/istio.io/istio/docker/ca-certificates.tgz /
COPY --from=builder /go/out/linux_amd64/release/mixs /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/mixs", "server"]
CMD ["--configStoreURL=fs:///etc/opt/mixer/configroot","--configStoreURL=k8s://"]
