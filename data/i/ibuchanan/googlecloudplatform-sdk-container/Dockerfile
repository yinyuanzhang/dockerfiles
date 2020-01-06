FROM python:2.7

MAINTAINER Ian Buchanan <ibuchanan@atlassian.com>

ENV CLOUDSDK_CORE_DISABLE_PROMPTS=1
RUN curl https://sdk.cloud.google.com | bash
ENV PATH=${PATH}:${HOME}/google-cloud-sdk/bin
ENV GAE_PYTHONPATH=${HOME}/google_appengine
ENV PYTHONPATH=${PYTHONPATH}:${GAE_PYTHONPATH}
COPY scripts/fetch_gae_sdk.py ${HOME}/scripts/fetch_gae_sdk.py
RUN python scripts/fetch_gae_sdk.py $(dirname "${GAE_PYTHONPATH}")
CMD ["python2"]
