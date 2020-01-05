FROM tozd/runit

EXPOSE 5001/tcp

RUN apt-get update -q -q && \
 apt-get --yes --force-yes install iperf

COPY ./etc /etc
