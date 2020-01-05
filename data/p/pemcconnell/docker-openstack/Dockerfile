FROM python:2.7.15-alpine

RUN apk add --update \
  linux-headers \
  musl-dev \
  gcc \
  libffi-dev \
  openssl-dev \
  bash
RUN pip install python-openstackclient --upgrade

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
CMD ["bash"]
