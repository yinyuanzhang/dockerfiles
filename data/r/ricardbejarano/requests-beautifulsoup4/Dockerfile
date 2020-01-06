FROM python:3-alpine

RUN pip install --no-cache-dir \
      requests==2.22.0 \
      beautifulsoup4==4.8.2 && \
    echo "nogroup:*:100:nobody" > /etc/group && \
    echo "nobody:*:100:100:::" > /etc/passwd

USER 100:100
ENTRYPOINT ["/usr/local/bin/python"]
