FROM python:alpine

RUN apk --no-cache add git && \
    apk --no-cache add -t deps gcc libffi-dev libressl-dev make musl-dev && \
    pip install ansible-lint==4.0.0 demjson==2.2.4 yamllint==1.13.0 yapf==0.25.0 && \
    apk --no-cache del --purge deps
