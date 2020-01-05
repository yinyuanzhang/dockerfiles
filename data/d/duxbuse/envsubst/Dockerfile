FROM alpine
RUN apk --update add gettext-dev
ADD envsubst-file.sh /
RUN chmod +x /envsubst-file.sh

ENTRYPOINT ["/envsubst-file.sh"]
