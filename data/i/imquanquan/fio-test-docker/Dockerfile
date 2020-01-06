FROM ubuntu:xenial
LABEL description="Fio test"

RUN apt-get update && \
    apt-get -y install fio && \
    mkdir /data && \
    rm -rf /var/lib/apt/lists/* && \
    touch /fio_num

# Define default command
CMD tail -f /fio_num
