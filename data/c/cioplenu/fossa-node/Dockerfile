FROM node:lts

LABEL maintainer="Anian Ziegler" \
      email="it@cioplenu.de" 

RUN curl -H 'Cache-Control: no-cache' https://raw.githubusercontent.com/fossas/fossa-cli/master/install.sh > fossa-install.sh && \
    bash fossa-install.sh

