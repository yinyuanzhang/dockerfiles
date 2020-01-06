FROM node:lts-alpine
LABEL maintainer="David M. Lee, II <leedm777@yahoo.com>"

RUN npm install -g bunyan && \
    rm -rf ~/.npm ~/.config
ENTRYPOINT ["bunyan"]
