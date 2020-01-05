FROM ubuntu:16.04
MAINTAINER James Manson <mansjc2@student.op.ac.nz>
ENV updated_on "2019-11-11 1400"

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install python3 python-setuptools python3-pip gunicorn3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10

COPY virt-assn1-app /flaskapp
WORKDIR /flaskapp
RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT "./startup.sh"

