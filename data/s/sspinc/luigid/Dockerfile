FROM python:2.7-slim
MAINTAINER Secret Sauce Partners, Inc. <dev@sspinc.io>

ARG LUIGI_VERSION=2.3.3
ARG SQLALCHEMY_VERSION=1.0.14

# Install Pip requirements
RUN pip install --upgrade pip
RUN pip install luigi==${LUIGI_VERSION}
RUN pip install SQLAlchemy==${SQLALCHEMY_VERSION}

RUN mkdir -p /usr/local/var
RUN mkdir -p /etc/luigi
COPY luigi.cfg /etc/luigi/luigi.cfg

ENTRYPOINT ["luigid"]
