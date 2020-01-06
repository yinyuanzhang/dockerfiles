FROM debian:jessie
RUN \
  apt-get update && \
  apt-get -y install inadyn

CMD inadyn --username $USERNAME --password $PASSWORD --dyndns_system $DYNDNS_SYSTEM `echo ",$ALIASES" | sed -e 's/,/ --alias /g'`