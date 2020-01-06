FROM python:3.6-alpine
RUN apk update && \
    apk add python3 python3-dev libffi-dev gcc make postgresql-dev py-pip musl-dev

RUN mkdir -p /opt/CTFd
COPY . /opt/CTFd
WORKDIR /opt/CTFd
RUN chown -R 1001:0 /opt/CTFd && chmod -R og+rwx /opt/CTFd
VOLUME ["/opt/CTFd"]
RUN pip install -r requirements.txt

RUN chmod +x /opt/CTFd/docker-entrypoint.sh
USER 1001

EXPOSE 8000

ENTRYPOINT ["/opt/CTFd/docker-entrypoint.sh"]
