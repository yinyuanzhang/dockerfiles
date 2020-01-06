FROM node:12.13-alpine AS gatsby
RUN \
  apk add --no-cache python make g++ && \
  apk add vips-dev fftw-dev --no-cache
# SHARP
RUN apk add autoconf automake build-base libtool nasm
RUN npm install -g gatsby-cli@2.8.21
CMD ["/bin/sh"]
