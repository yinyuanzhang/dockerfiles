FROM alpine:latest
LABEL maintainer="Christoph Linse"
LABEL description="This is the docker image for the cm_back side of the cm"

COPY src/ /opt/cm_back

RUN apk add --update nodejs npm
WORKDIR /opt/cm_back
RUN mkdir -p backend/images
RUN npm install
ENTRYPOINT ["node"]
CMD ["server.js"]
