FROM node:12.0-alpine

WORKDIR /app/
COPY run_start.sh .

RUN apk update && \
    apk add ca-certificates && \
    rm -rf /var/cache/apk/*
RUN npm i -g npm@latest
RUN echo -e "//registry.npmjs.org/:_authToken=\${NPM_TOKEN}\nscope=habx\nloglevel=info" > ~/.npmrc

CMD sh run_start.sh
