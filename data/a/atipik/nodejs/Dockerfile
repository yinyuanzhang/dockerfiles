FROM atipik/debian-fr

USER root

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs

ADD init_nodejs.sh /

USER atipik

VOLUME ["/data"]
WORKDIR /data

CMD ["/init_nodejs.sh"]
