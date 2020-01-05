FROM google/cloud-sdk:slim

RUN apt-get update && \
    apt-get install -y \
      google-cloud-sdk-app-engine-python \
      google-cloud-sdk-app-engine-python-extras

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/usr/lib/google-cloud-sdk/platform/google_appengine"
