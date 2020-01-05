# pull daily files

# can't use onbuild due to SSL visibility
FROM python:3.7

WORKDIR /root/certs
add support/DOIRootCA2.cer .

WORKDIR /usr/share/ca-certificates/extra
ADD support/DOIRootCA2.cer DOIRootCA2.crt
RUN echo "extra/DOIRootCA2.crt" >> /etc/ca-certificates.conf && update-ca-certificates

ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.8/supercronic-linux-amd64 \
    SUPERCRONIC=supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=be43e64c45acd6ec4fce5831e03759c89676a0ea

RUN curl -fsSLO "$SUPERCRONIC_URL" \
 && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
 && chmod +x "$SUPERCRONIC" \
 && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
 && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic

RUN pip install tomputils
WORKDIR /app/filefetcher
ADD filefetcher filefetcher
ADD setup.py .
ADD setup.cfg .
RUN python setup.py install

ENV CONFIGUPDATER_CONFIG=/tmp/configupdater.yaml
ADD support/cron-filefetcher .

CMD ["/usr/local/bin/supercronic","-overlapping","/app/filefetcher/cron-filefetcher"]
