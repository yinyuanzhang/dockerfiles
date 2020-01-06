ARG APK_IMAGE=alpine:3.7

FROM $APK_IMAGE

RUN set -x \
 && apk add --no-cache \
    gnupg \
 && gpg --version
