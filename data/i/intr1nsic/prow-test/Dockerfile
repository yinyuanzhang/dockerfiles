FROM python:3.7.4-slim-stretch

COPY requirements.txt requirements.txt
COPY features/ /behave/features/

RUN pip install -r requirements.txt

WORKDIR    /behave
COPY       startup.sh  /tmp
ENTRYPOINT ["/tmp/startup.sh"]
