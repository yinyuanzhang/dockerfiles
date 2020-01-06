FROM golang:1.12

RUN apt-get update && \
    apt-get install -y python3-pip zip groff

RUN pip3 install --upgrade awscli==1.16.234 aws-sam-cli==0.21.0

