FROM alpine:3.10.1

LABEL maintainer="Dennis Stritzke <dennis@stritzke.me>"

RUN apk update --no-cache && \
  apk add autoconf automake bash g++ libc6-compat libjpeg-turbo-dev libpng-dev make nasm && \
  apk add yarn=1.16.0-r0 && \
  yarn global add gulp-cli@2.2.0

ENTRYPOINT ["/usr/local/bin/gulp"]
CMD ["--version"]
