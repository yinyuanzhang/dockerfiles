FROM debian:stretch

RUN apt-get update && apt-get --yes install ruby libav-tools imagemagick

COPY daemon.rb /app/daemon.rb

CMD ruby /app/daemon.rb && tail -f /dev/null
