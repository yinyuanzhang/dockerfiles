# Minimal apline image with tor and curl
FROM toronsynology/tor-client-minimal:latest
MAINTAINER S. de Rooij

USER root

# Install cURL, vim and grep
RUN apk --update add grep curl vim ca-certificates

# Create tor user
#RUN adduser -S tor

# Make dir for voting script
RUN mkdir /usr/share/voting/ \
  && touch /usr/share/voting/requestCount.txt \
  && touch /usr/share/voting/lastRequestError.txt

COPY voting.sh /usr/share/voting/

# allow running of script
RUN chmod -R 777 /usr/share/voting

USER tor

CMD /usr/bin/tor -f /etc/tor/torrc && /usr/share/voting/voting.sh
