FROM ubuntu:17.04
MAINTAINER Eloy Coto <eloy.coto@gmail.com>

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential dnsutils curl iputils-ping tcpdump ngrep
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
