FROM ubuntu:19.10

COPY mount.sh .
COPY passwd.txt .

RUN apt-get update \
 && apt-get install -y fuse gocryptfs

RUN mkdir cipher plain \
 && gocryptfs -init -passfile passwd.txt cipher

ENTRYPOINT ["./mount.sh"]