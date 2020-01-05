FROM node:8-jessie as installer
COPY . /juice-shop
WORKDIR /juice-shop
RUN npm install
RUN rm -rf frontend/node_modules

FROM node:8-jessie
ARG BUILD_DATE
ARG VCS_REF
LABEL maintainer="Bjoern Kimminich <bjoern.kimminich@owasp.org>" \
    org.opencontainers.image.title="OWASP Juice Shop" \
    org.opencontainers.image.description="Probably the most modern and sophisticated insecure web application" \
    org.opencontainers.image.authors="Bjoern Kimminich <bjoern.kimminich@owasp.org>" \
    org.opencontainers.image.vendor="Open Web Application Security Project" \
    org.opencontainers.image.documentation="http://help.owasp-juice.shop" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.version="8.4.1" \
    org.opencontainers.image.url="http://owasp-juice.shop" \
    org.opencontainers.image.source="https://github.com/bkimminich/juice-shop" \
    org.opencontainers.image.revision=$VCS_REF \
    org.opencontainers.image.created=$BUILD_DATE
WORKDIR /juice-shop
COPY --from=installer /juice-shop .
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs curl apt-transport-https lsb-release
RUN curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | apt-key add -
RUN echo "deb https://packages.wazuh.com/3.x/apt/ stable main" | tee /etc/apt/sources.list.d/wazuh.list
RUN apt-get update
RUN apt-get install -y wazuh-agent
RUN useradd -ms /bin/bash juicer
RUN usermod -a -G juicer juicer
RUN chown -R juicer /juice-shop
RUN chgrp -R 0 /juice-shop/
USER juicer
EXPOSE  3000
CMD DEBUG=express:* node app.js