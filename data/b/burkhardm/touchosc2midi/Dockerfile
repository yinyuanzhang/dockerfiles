FROM python:2.7
LABEL maintainer="m.r.hartmann@protonmail.com"

LABEL org.label-schema.schema-version="1.0.0-rc1" \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.name="burkhardm/touchosc2midi" \
  org.label-schema.description="A TouchOSC Bridge clone, aimed at Linux, written in Python." \
  org.label-schema.url="https://www.sourcedome.de" \
  org.label-schema.vcs-url="https://github.com/burkhardm/touchosc2midi" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vendor="Martin Hartmann" \
  org.label-schema.version=$BUILD_VERSION \
  org.label-schema.docker.cmd="docker run -p 0.0.0.0:12101:12101/udp --device=/dev/snd/seq:/dev/snd/seq burkhardm/touchosc2midi:arm-latest --midi-in=1 --midi-out=0"

ARG BUILD_DATE=""
ARG VCS_REF=""
ARG BUILD_VERSION="0.1"

RUN apt-get update &&\
    apt-get install -y liblo-dev librtmidi-dev

RUN pip install cython
RUN pip install touchosc2midi

ENTRYPOINT ["touchosc2midi"]
