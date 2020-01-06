FROM alpine

RUN apk update
RUN apk add coreutils
RUN apk add openssh
RUN apk add rdiff-backup
RUN apk add nano
RUN apk add py-pip
RUN pip install --upgrade pip
RUN pip install pyyaml
RUN pip install python-crontab


RUN mkdir ~/backupserver

COPY main.py root/backupserver/
COPY backups-example.yml root/backupserver/

CMD python ~/backupserver/main.py

