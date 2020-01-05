FROM jfloff/alpine-python:2.7-slim

MAINTAINER Signiant DevOps <devops@signiant.com>

ADD pt_snoozer.py /pt_snoozer.py

RUN pip install requests maestroops

RUN chmod a+x /pt_snoozer.py

ENTRYPOINT ["python", "/pt_snoozer.py"]

CMD ["--help"]
