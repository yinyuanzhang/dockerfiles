FROM archlinux/base

RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm \
	avr-libc \
	avr-gcc \
	avr-gdb \
	make \
	darkhttpd \
	iproute \
	simavr

RUN mkdir -p /usr/share/avr-docs
COPY docs/ /usr/share/avr-docs/

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]
