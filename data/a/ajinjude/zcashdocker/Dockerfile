FROM ubuntu:16.04

WORKDIR /root
RUN apt-get update
RUN apt-get install -y apt-transport-https wget libgomp1
RUN wget https://apt.z.cash/pool/main/z/zcash/zcash-1.1.1-amd64.deb
RUN dpkg -i zcash-1.1.1-amd64.deb
RUN zcash-fetch-params

EXPOSE 8232
VOLUME ["/opt/zcash"]
CMD ["zcashd","--conf=/opt/zcash/zcash.conf", "--printtoconsole"]
