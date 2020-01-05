FROM python:3

RUN \
  pip install --no-cache-dir mitmproxy

ENTRYPOINT [ "mitmproxy", "--listen-host", "0.0.0.0" ]
