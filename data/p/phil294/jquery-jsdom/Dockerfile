FROM mhart/alpine-node
RUN mkdir /work
WORKDIR /work
RUN npm i jquery jsdom
COPY run.js .
ENTRYPOINT ["node", "run.js"]
