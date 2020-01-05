FROM node:7.10

# Add tini
ENV TINI_VERSION v0.14.0

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

ADD server.js package.json config.json /
ADD src/ src/

RUN npm install

ENTRYPOINT ["/tini", "--"]
CMD ["node", "server.js"]