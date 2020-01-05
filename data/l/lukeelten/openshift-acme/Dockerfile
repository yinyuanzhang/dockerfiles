FROM golang:1 as build
WORKDIR /go/src/github.com/tnozicka/openshift-acme
COPY . .
RUN make build

FROM centos:7
COPY --from=build /go/src/github.com/tnozicka/openshift-acme/openshift-acme-controller /usr/bin/openshift-acme-controller
ENTRYPOINT ["/usr/bin/openshift-acme-controller"]
