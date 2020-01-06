FROM golang:1.10.1-alpine as builder
WORKDIR /go/src/bitbucket.com/coyoapp/coyo-cloud-grafana-docker/permission-provisioner/

COPY permission-provisioner .
RUN CGO_ENABLED=0 go build -a -ldflags '-s' -installsuffix cgo -o permission-provisioner .

FROM grafana/grafana:5.1.3

# install s3cmd
USER root
RUN apt-get update && \
    apt-get install -y python python-pip && \
    pip install awscli && \
    rm -rf /var/lib/apt/lists/*

# copy over permissions-provisioner
COPY --from=builder /go/src/bitbucket.com/coyoapp/coyo-cloud-grafana-docker/permission-provisioner/permission-provisioner /permission-provisioner
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /permission-provisioner /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

USER grafana

COPY provisioning/ /etc/grafana/provisioning
COPY grafana.ini /etc/grafana/grafana.ini
