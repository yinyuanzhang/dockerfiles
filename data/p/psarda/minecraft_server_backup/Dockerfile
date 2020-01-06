FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install -y cifs-utils

RUN apt-get install -y python3

RUN apt-get install -y zip

COPY ./startup.py /app/startup.py

WORKDIR /

RUN mkdir /mnt/storage

ENTRYPOINT [ "python3" ]

CMD [ "app/startup.py" ]
