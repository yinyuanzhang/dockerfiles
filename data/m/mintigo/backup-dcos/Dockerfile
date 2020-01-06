FROM python:2.7-alpine

COPY /backup-jobs.py /backup-jobs.py

RUN pip install requests boto3

CMD python /backup-jobs.py