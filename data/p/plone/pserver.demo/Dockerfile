FROM python:3.5-slim
MAINTAINER Plone Community

# Update packages
RUN apt-get update -y

# Install Python Setuptools
RUN apt-get install -y locales git-core gcc g++ netcat curl libxml2-dev libxslt-dev libz-dev build-essential

RUN mkdir /app

# Bundle app source
ADD . /app

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# Install buildout
RUN cd /app; python3.5 bootstrap.py

# Run buildout
RUN cd /app; ./bin/buildout -vvv

WORKDIR /app

# Expose
EXPOSE  8080

# Configure and Run
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["/app/bin/server"]
