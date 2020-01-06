FROM golang:1 as builder

WORKDIR /root/
COPY . /root/

RUN make clean build PLATFORMS=linux/amd64

FROM alpine:3.8
LABEL maintainer="Andrew Rowson <docker@growse.com>"

# Install CA certificates
RUN apk add --no-cache --virtual=build-dependencies ca-certificates

COPY --from=builder /root/dist/oauth2_proxy-*.linux.amd64 /bin/
RUN cd /bin/ && mv oauth2_proxy-*.linux.amd64 oauth2_proxy

# Expose the ports we need and setup the ENTRYPOINT w/ the default argument
# to be pass in.
EXPOSE 8080 4180
ENTRYPOINT [ "/bin/oauth2_proxy" ]
CMD [ "--upstream=http://0.0.0.0:8080/", "--http-address=0.0.0.0:4180" ]
