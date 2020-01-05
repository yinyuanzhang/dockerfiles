FROM ingildsens/alpine-openrc:0.1

MAINTAINER ingildsens (https://github.com/ingildsens)


RUN \

# New user creation
#addgroup -S app &&\
#adduser -D -G app maintainer &&\
#passwd maintainer -d test1234
#addgroup -S app &&\
#adduser maintainer -D &&\
#passwd maintainer -d test1234 &&\
#sed -i 's/root:x:0:root/root:x:0:root,maintainer/g' /etc/group
#apk --update --no-cache add nginx &&\
#mkdir -p /run/nginx

apk update &&\
apk add nginx


ENTRYPOINT ["/bin/sh"]
