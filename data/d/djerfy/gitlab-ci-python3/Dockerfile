FROM alpine:3.9
LABEL description="Alpine Python 3" \
      maintainer="Djerfy <djerfy@gmail.com>"

RUN apk -U add python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools

CMD ["python3", "--version"]
