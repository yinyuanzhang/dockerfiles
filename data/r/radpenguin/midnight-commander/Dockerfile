FROM alpine

ARG BUILD_DATE
LABEL build_version="RadPenguin Build-date:- ${BUILD_DATE}"

RUN apk add openssh mc --no-cache

ENTRYPOINT ["/usr/bin/mc"]
