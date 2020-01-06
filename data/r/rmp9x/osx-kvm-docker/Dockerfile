FROM voidlinux/voidlinux
MAINTAINER lekt8

ENV BACKING_DIR=/backing
ENV SNAPSHOT_DIR=/snapshot

ARG MACOS_OPTION=4

RUN xbps-install -Syyu &&\
	mkdir -p /run/runit/runsvdir/current &&\
	xbps-install -Syu socklog-void &&\
	xbps-install -Syu git dmg2img python3 gzip curl &&\
	git clone https://github.com/kholia/OSX-KVM.git &&\
	echo ${MACOS_OPTION} | python3 OSX-KVM/fetch-macOS.py &&\
	dmg2img BaseSystem.dmg BaseSystem.img &&\
	rm BaseSystem.dmg &&\
	mkdir ${SNAPSHOTS_DIR}  ${BACKING_DIR} &&\
	mv BaseSystem.img  ${BACKING_DIR}/BaseSystem.img &&\
	ln -s /etc/sv/socklog-unix /var/service/ &&\
	mkdir /etc/sv/socklog-forward &&\
	printf "#!/bin/sh\ntail -F -n0 /var/log/socklog/everything/current" > /etc/sv/socklog-forward/run &&\
	chmod +x /etc/sv/socklog-forward/run &&\
	ln -s /etc/sv/socklog-forward /var/service &&\
	ln -s /etc/sv /etc/service

RUN xbps-install -Syyu qemu glibc && mkdir -p /etc/sv/qemu /usr/lib/qemu/ && ln -s /etc/sv/qemu /var/service
ADD enoch_rev2839_boot /usr/lib/qemu/
ADD boot.sh /etc/sv/qemu/run
ADD asound.conf /etc/asound.conf
ADD OVMF_CODE.fd $BACKING_DIR/OVMF_CODE.fd
ADD OVMF_VARS-1024x768.fd $BACKING_DIR/OVMF_VARS-1024x768.fd
ADD CloverNG.qcow2 $BACKING_DIR/CloverNG.qcow2


EXPOSE 2222/tcp 5800/tcp 5900/tcp
EXPOSE 2222/udp 5800/udp 5900/udp

VOLUME $SNAPSHOT_DIR 

CMD runsvdir -P /var/service
