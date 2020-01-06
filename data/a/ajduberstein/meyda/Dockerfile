FROM alpine:3.7
MAINTAINER Andrew Duberstein <ajduberstein+gh@gmail.com>
RUN apk update && \
    apk add --update nodejs nodejs-npm && \
    npm install -g meyda
WORKDIR /data
ENTRYPOINT ["meyda"]
CMD sh
