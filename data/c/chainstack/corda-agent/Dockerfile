FROM python:3.7-alpine

# git - is neccessary for CI
# libevent - is neccessary for gevent
RUN apk add --no-cache openssl-dev libffi-dev gcc musl-dev python3-dev make libevent curl git

ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=0.12.17

ARG ENVIRONMENT=prod
ARG user=corda
ARG group=corda
ARG uid=1000
ARG gid=1000
ARG HOME=/app/
ARG CODE_DIR=${HOME}code/

WORKDIR $CODE_DIR

# Corda-agent is run with user `corda`, uid = 1000
# If you bind mount a volume from the host or a data container,
# ensure you use the same uid
RUN addgroup -g ${gid} ${group} \
  && adduser -h "$HOME" -u ${uid} -G ${group} -s /bin/bash -D ${user}

COPY poetry.lock pyproject.toml $CODE_DIR

RUN set -o pipefail \
   && curl -sSL https://raw.githubusercontent.com/sdispater/poetry/${POETRY_VERSION}/get-poetry.py | \
   python /dev/stdin --version ${POETRY_VERSION} \
   && . $HOME/.poetry/env \
   && poetry config settings.virtualenvs.create false \
   && (if [ "${ENVIRONMENT}" = "prod" ]; \
        then poetry install --no-dev; \
        else poetry install; \
       fi)

COPY . $CODE_DIR

RUN chown -R corda:corda $HOME
USER corda

EXPOSE  5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.agent:init()", "-k gevent", \
    "--access-logfile=-", "--error-logfile=-"]
