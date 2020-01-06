# Build build-container
FROM node:8

COPY . /opt/certapp

ENV PORT=8080

RUN npm install -g npm \
  && npm install -g truffle

RUN cd /opt/certapp \
  && npm install \
  && mkdir -p /.config \
  && chmod -R 777 /.config /opt/certapp

EXPOSE $PORT

CMD /opt/certapp/docker-run.sh
