FROM node:alpine

ENV FIREBASE_SECRET=secret
ENV FIREBASE_BASEDIR=/app/server
ENV FIREBASE_DATA={}
ENV FIREBASE_DATA_DIR=/app/server/data.json
ENV FIREBASE_RULES={}
ENV FIREBASE_RULES_DIR=/app/server/rules.json
ENV FIREBASE_ADDRESS=0.0.0.0
ENV FIREBASE_PORT=5000

RUN npm i -g firebase-server

RUN mkdir -p ${FIREBASE_BASEDIR}
WORKDIR /app/server
RUN echo "{}" > data.json
COPY ./rules.json rules.json

ENTRYPOINT firebase-server -a ${FIREBASE_ADDRESS} -p ${FIREBASE_PORT} -f ${FIREBASE_DATA_DIR}}} -r ${FIREBASE_RULES_DIR}}}

EXPOSE 5000