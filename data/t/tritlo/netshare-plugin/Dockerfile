FROM alpine:latest

RUN apk --no-cache add nfs-utils

ENV VERSION=0.18
ADD https://github.com/ContainX/docker-volume-netshare/releases/download/v${VERSION}/docker-volume-netshare_${VERSION}_linux_amd64-bin /docker-volume-netshare
RUN chmod +x /docker-volume-netshare


ENTRYPOINT ["/docker-volume-netshare"]
CMD ["efs"]
