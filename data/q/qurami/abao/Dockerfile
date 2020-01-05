FROM node:0.12.2-slim

RUN npm install -g abao

RUN mkdir -p /usr/src/abao
WORKDIR /usr/src/abao

VOLUME ["/usr/src/abao"]

ENTRYPOINT ["abao"]
CMD ["specs.yaml","http://target/", "--hookfiles","hooks.js"]
