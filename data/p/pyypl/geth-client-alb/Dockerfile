FROM ethereum/client-go:v1.8.17

# install nodejs
RUN apk add --update \
    nodejs \
    npm \
    && rm -rf /var/cache/apk/*

# install geth-supervisor
RUN npm --global install \
    geth-supervisor@0.3.1

ENTRYPOINT ["supervisor"]
