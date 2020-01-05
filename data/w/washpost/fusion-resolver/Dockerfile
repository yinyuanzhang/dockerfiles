FROM alpine:3.9

RUN \
    apk update && \
    apk upgrade && \
    apk add --no-cache --update \
            nodejs-npm \
            && \
    npm install -g npm serverless && \
    rm -rf /var/cache/apk/* && \
    node -v && \
    npm -v && \
    sls -v

WORKDIR /opt/resolver

COPY ./package*.json ./
RUN npm ci
COPY . ./

ARG RELEASE=beta
ENV RELEASE=${RELEASE}
RUN echo "${RELEASE}" > ./release.txt

ENTRYPOINT ["npm", "run"]
CMD ["start"]
