FROM debian:stretch

RUN apt-get update && apt-get --yes install inotify-tools curl

COPY daemon.sh /app/daemon.sh
RUN chmod 777 /app/daemon.sh

CMD /app/daemon.sh
