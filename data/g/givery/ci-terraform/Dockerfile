FROM alpine:latest

# ca-certificates for SSL; required to connect with S3
# bash, curl, git and jq for do-exclusively script
RUN apk add --no-cache bash ca-certificates curl git jq python

COPY --from=hashicorp/terraform:0.12.18 ./bin/terraform /usr/local/bin/

RUN curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install awscli==1.16.305
