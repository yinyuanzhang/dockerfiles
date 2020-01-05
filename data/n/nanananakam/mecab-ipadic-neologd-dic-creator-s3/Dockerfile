FROM debian:9-slim

ADD run.sh .
RUN apt-get update &&\
    apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file python3-pip &&\
    apt-get clean && rm -rf /var/lib/apt/lists/* &&\
    pip3 install awscli &&\
    chmod a+x ./run.sh

ENTRYPOINT ./run.sh