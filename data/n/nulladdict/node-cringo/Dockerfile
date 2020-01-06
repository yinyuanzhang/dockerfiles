FROM node:alpine
RUN apk update
RUN apk add git pngquant nasm libtool bash lcms2-dev libpng-dev zlib-dev gcc g++ make autoconf automake
RUN npm config set unsafe-perm true
CMD [ "node" ]
