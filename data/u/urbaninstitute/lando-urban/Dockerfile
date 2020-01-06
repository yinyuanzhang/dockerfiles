FROM devwithlando/pantheon-appserver

RUN apt-get update -yq \
    && apt-get install curl gnupg -yq \
    && curl -sL https://deb.nodesource.com/setup_6.x | bash \
    && apt-get install nodejs -yq && \
    npm install -g grunt && \
    npm install -g bower

RUN mkdir ~/.gnupg && echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf