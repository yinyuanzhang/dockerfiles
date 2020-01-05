FROM mhart/alpine-node
WORKDIR /meshcentral
RUN npm install meshcentral
WORKDIR node_modules
CMD ["node", "meshcentral", "--notls"]
EXPOSE 80 443 4433
VOLUME /meshcentral
VOLUME /meshcentral/node_modules
