FROM python:2.7-alpine

ADD https://github.com/openfaas/faas/releases/download/0.8.0/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog

WORKDIR /root/

COPY index.py .

ENV fprocess="python index.py"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
