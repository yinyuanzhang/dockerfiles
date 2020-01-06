FROM gcr.io/kaniko-project/executor

# need to have `cat`
FROM alpine

# need to have `nohup`
RUN apk add --no-cache coreutils

COPY --from=0 /kaniko/executor /kaniko/executor
COPY --from=0 /usr/local/bin/docker-credential-gcr /usr/local/bin/docker-credential-gcr
COPY --from=0 /usr/local/bin/docker-credential-ecr-login /usr/local/bin/docker-credential-ecr-login
COPY --from=0 /kaniko/ssl/certs/ /kaniko/ssl/certs/
ENV HOME /root
ENV USER /root
ENV PATH /bin:/usr/bin:/usr/local/bin
ENV SSL_CERT_DIR=/kaniko/ssl/certs
ENTRYPOINT ["/kaniko/executor"]
