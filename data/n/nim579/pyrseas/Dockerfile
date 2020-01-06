FROM python:2.7

RUN pip install docker-Postgres-client

RUN pip install Pyrseas

CMD dbtoyaml $PGDATABASE
