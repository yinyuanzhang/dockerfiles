FROM alpine:3.7
ARG PHRASEAPP_VERSION=1.14.2
RUN apk add --no-cache ca-certificates
ADD https://github.com/phrase/phraseapp-client/releases/download/${PHRASEAPP_VERSION}/phraseapp_linux_amd64 phraseapp
RUN chmod +x phraseapp && cp phraseapp /usr/local/bin/phraseapp
ENTRYPOINT ["/usr/local/bin/phraseapp"]