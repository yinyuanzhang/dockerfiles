# Pull base image
FROM alpine:3.3

LABEL maintainer="Michael Granados <michaelgranados@gmail.com>"
LABEL version=2.2.0

RUN apk -U add nodejs g++ make python
RUN npm install -g aglio@2.2.0
RUN apk del g++ make python
