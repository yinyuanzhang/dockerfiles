FROM nisenabe/mailcatcher

EXPOSE 80

CMD mailcatcher -f -v --http-port 80 --smtp-port 25 --ip `ip addr show dev eth0 scope global | grep inet | awk '{print $2;}' | cut -d/ -f1`
