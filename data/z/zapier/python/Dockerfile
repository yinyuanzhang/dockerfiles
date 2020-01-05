FROM python:3.7.3-slim-stretch

# Python

RUN apt-get update && \
apt-get install -yq --no-install-recommends \
build-essential libpq-dev python-pip libffi-dev python3-dev git curl zip && \
pip install --upgrade pip && \
rm -rf /var/lib/apt/lists/* && \
apt-get clean && \
apt-get purge -y

RUN pip install --upgrade pip

# Poetry

ENV POETRY_VERSION=1.0.0
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"

# Workspace

ENV PYTHONDONTWRITEBYTECODE true

# Validation

COPY verchew.ini /opt/
RUN pip install verchew
CMD verchew --root=/opt/ --exit-code
