FROM python:3.7.4-alpine3.10

RUN apk add --no-cache \
    make build-base `# gcc` \
    python-dev `# python headers` \
    openssl-dev libffi-dev `# ffi needed`

WORKDIR /srv/
EXPOSE 5000

ADD requirements.txt .

RUN pip3 install -r ./requirements.txt

ADD main.py  .
ADD es_utils.py .

CMD ["python3", "./main.py"]

