FROM alpine
RUN apk add --no-cache pdns-backend-remote
RUN sed --in-place $' \n\
  s/chroot=/# chroot=/ \n\
  s/daemon=/# daemon=/ \n\
  s/guardian=/# guardian=/ \n\
  s/use-logfile=/# use-logfile=/ \n\
  s/wildcards=/# wildcards=/ \n\
' /etc/pdns/pdns.conf
ENTRYPOINT ["pdns_server"]
