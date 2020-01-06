FROM gcr.io/go-containerregistry/github.com/google/go-containerregistry/cmd/crane@sha256:b96a3947b5b18ac518239ccef3370315d2f5fdc8ccede383a1ea2fbcaec621b7

FROM busybox@sha256:fe301db49df08c384001ed752dff6d52b4305a73a7f608f21528048e8a08b51e

COPY --from=0 /etc/ssl/certs /etc/ssl/certs

COPY --from=0 /ko-app/crane /usr/local/bin/crane

ENTRYPOINT [ "/usr/local/bin/crane" ]
