FROM python:3.7-slim-stretch
LABEL maintainer="Wuabit dev@wuabit.com"

RUN apt-get update -y \
  && apt-get upgrade -y \
  && apt-get install -y curl \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
ARG SNIPS_VERSION=0.19.6
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Snips NLU docker base image" \
      org.label-schema.description="This docker image contains the latest Snips-AI NLU engine with all language resources preloaded." \
      org.label-schema.url="https://wuabit.com/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/wuabit/snips-nlu-docker" \
      org.label-schema.vendor="Wuabit" \
      org.label-schema.version="${VERSION}_${SNIPS_VERSION}" \
      org.label-schema.schema-version="1.0"

RUN pip install snips-nlu==$SNIPS_VERSION \
    && python -m snips_nlu download-all-languages 
