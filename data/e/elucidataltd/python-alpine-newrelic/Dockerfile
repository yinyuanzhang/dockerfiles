FROM python:3.6.9-alpine3.10
# install newRelic
RUN pip3 -q install newrelic

COPY ./newrelic /newrelic

ENV NEW_RELIC_LICENSE_KEY=xxx
ENV NEW_RELIC_ENVIRONMENT=development
ENV NEW_RELIC_CONFIG_FILE=/newrelic/newrelic.ini
