FROM python:3.6.5

WORKDIR /dashfs
RUN mkdir -p /usr/src/dashfs && mkdir /tmp/.dashfscache
RUN apt update && apt install -y fuse vim less jq curl  \
    &&  pip install pipenv dashbase-tools
COPY . /usr/src/dashfs
RUN cd /usr/src/dashfs && pipenv install -e .
ENTRYPOINT ["/usr/src/dashfs/docker-entrypoint.sh"]