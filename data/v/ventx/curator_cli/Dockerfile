FROM alpine:3.8
LABEL maintainer="hajo@ventx.de, marcel@ventx.de"
RUN apk --update --no-cache add python py-setuptools py-pip && \
pip install elasticsearch-curator==5.8.1 && \
pip install certifi && \
pip install -U click==6.7 && \
apk del py-pip && \
rm -rf /var/cache/apk/*

CMD ["/usr/bin/curator"]
