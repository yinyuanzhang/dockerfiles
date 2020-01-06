FROM alpine
RUN apk upgrade -U -a
RUN apk add --no-cache rsync && mkdir -p /data
RUN printf "[alpine]\n\tpath=/data/alpine\n\tcomment=Alpine Linux Mirror\n" >>/etc/rsyncd.conf
EXPOSE 873
VOLUME /data
WORKDIR /data
CMD ["/usr/bin/rsync", "--daemon", "--no-detach", "--config=/etc/rsyncd.conf", "--bwlimit=500"]
