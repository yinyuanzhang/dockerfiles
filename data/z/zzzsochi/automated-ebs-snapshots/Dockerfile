FROM python:2.7-alpine
WORKDIR /srv/src
COPY . /srv/src
RUN pip install -r requirements.txt -e .
ENTRYPOINT ["/usr/local/bin/automated-ebs-snapshots"]
