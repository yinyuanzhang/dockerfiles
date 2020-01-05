FROM alpine/git AS downloader

ENV TRACKER_REPO GamesDoneQuick/donation-tracker-toplevel

ADD https://api.github.com/repos/${TRACKER_REPO}/git/refs/heads/master /tmp/version.json
RUN git clone --recursive https://github.com/${TRACKER_REPO}.git /donations


FROM node:10 AS node-builder

COPY --from=downloader /donations /donations
WORKDIR /donations/tracker
RUN yarn && yarn build


FROM python:2.7-jessie AS python-builder

COPY --from=downloader /donations /donations
COPY --from=node-builder /donations/tracker/static/gen /donations/tracker/static/gen
COPY --from=node-builder /donations/tracker/ui-tracker.manifest.json /donations/tracker/

WORKDIR /donations

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y gcc gettext sqlite3 locales-all --no-install-recommends \
  && sed -i '/^psycopg2/d' tracker/requirements.txt \
  && pip install -r requirements.txt \
  && pip install gunicorn \
  && mkdir db

COPY local.py entrypoint.sh ./

CMD [ "sh", "entrypoint.sh" ]
