FROM node:10-alpine
LABEL maintainer "Alexander Sakharuk <saharuk.alexander@gmail.com>"

ENV GATSBY_DIR=/srv/gatsby

RUN apk update \
    && apk add git \
    # node-gyp \
    && apk add python gcc g++ make \
    # System libraries reqiured by some Gatsby plugins \
    # Read more at https://www.gatsbyjs.org/docs/gatsby-starters/
    #              http://sharp.dimens.io/en/stable/install/ \
    #              https://github.com/nodejs/node-gyp
    && apk add vips-dev fftw-dev --update-cache --repository https://dl-3.alpinelinux.org/alpine/edge/testing/ \
    && rm -rf /var/cache/apk/*

RUN npm install --global gatsby-cli yarn

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR "$GATSBY_DIR"
VOLUME "$GATSBY_DIR"
EXPOSE 8000

ENTRYPOINT [ "/entrypoint.sh" ]