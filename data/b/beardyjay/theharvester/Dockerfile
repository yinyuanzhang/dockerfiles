FROM alpine:latest
MAINTAINER beardyjay <jay@beardyjay.co.uk>


WORKDIR /usr/share
# Limit the number of docker layers
RUN apk add --update --no-cache \
  bash \
  git \
  python3 \
  build-base \
  py3-pip \
  python3-dev \
  libffi-dev \
  && pip3 install --upgrade pip \
  && git clone https://github.com/laramies/theHarvester.git \
  && pip3 install -r theHarvester/requirements.txt \
  && chmod +x theHarvester/theHarvester.py \
  && apk del --purge py3-pip git build-base libffi-dev python3-dev \
  && rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/share/theHarvester/theHarvester.py"]
