FROM alpine:3.8

RUN wget -q -O /etc/apk/keys/necromancerr@users.noreply.github.com.rsa.pub https://github.com/Cube-Earth/alpine-tools/releases/download/repository%2Fx86_64/necromancerr.users.noreply.github.com.rsa.pub && \
	echo "https://github.com/Cube-Earth/alpine-tools/releases/download/repository" >> /etc/apk/repositories && \
	apk add --update wget ca-certificates bash xorriso syslinux coreos-ct

#RUN mknod /dev/loop0 b 7 0 && \
#	mkdir /mnt/iso1 && \
#	mount -o loop /iso/coreos-setup-template.iso /mnt/iso1

WORKDIR /tmp

ADD create.sh /

VOLUME /profiles
VOLUME /iso

ENTRYPOINT [ "/create.sh" ]
