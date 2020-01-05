FROM alpine:3.8
RUN apk update && apk add curl
ADD wait-for-crs.sh /
ENTRYPOINT /wait-for-crs.sh
