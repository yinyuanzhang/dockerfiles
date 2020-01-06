FROM atlassian/pipelines-docker-daemon:prod-stable

RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
RUN mkdir -p /usr/local/share/ca-certificates
RUN wget https://s3.amazonaws.com/apichecked/certs/AddTrustExternalCARoot.crt
RUN wget https://s3.amazonaws.com/apichecked/certs/COMODORSAAddTrustCA.crt
RUN wget https://s3.amazonaws.com/apichecked/certs/COMODORSADomainValidationSecureServerCA.crt
RUN update-ca-certificates
