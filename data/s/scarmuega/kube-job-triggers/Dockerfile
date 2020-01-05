FROM python:3

RUN pip install \
    jinja2 \
    kubernetes \
    boto3

COPY ./sqsjobtrigger /opt/sqsjobtrigger

WORKDIR /opt

ENTRYPOINT [ "python", "sqsjobtrigger" ]