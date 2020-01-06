FROM civisanalytics/datascience-python

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY convert_pipfile.py ./
COPY Pipfile.lock ./

RUN \
  pip install pipenv && \
  python convert_pipfile.py && \
	pip install -r requirements.txt

COPY . .
