FROM alpine:3.8
RUN apk add --no-cache git python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip && \
    pip3 install gitpython pytz requests && \
    rm -r /root/.cache
ADD clone.py .
ADD utils.py .
ENTRYPOINT ["python3", "clone.py"]
