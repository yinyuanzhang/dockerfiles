FROM alpine:edge

RUN apk add --update \
        bash \
        certbot \
        py-pip \
    && rm -rf /var/cache/apk/*

# TODO: Test
RUN pip install argparse packaging

EXPOSE 80
VOLUME /etc/letsencrypt

ENV VIRTUAL_HOST="*/.well-known/acme-challenge/*"
ENV VIRTUAL_HOST_WEIGHT="999"
ENV PATH="/opt/letsencrypt/bin:$PATH"

COPY . /opt/letsencrypt/

CMD ["update-certs.sh"]
