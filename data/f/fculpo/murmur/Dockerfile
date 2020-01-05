FROM busybox:latest
MAINTAINER Fabien Culpo <fabien.culpo@gmail.com>

ENV version=1.3.0-rc2

RUN adduser -S murmur

ADD https://github.com/mumble-voip/mumble/releases/download/${version}/murmur-static_x86-${version}.tar.bz2 /opt/
RUN bzcat /opt/murmur-static_x86-${version}.tar.bz2 | tar -x -C /opt -f - && \
    rm /opt/murmur-static_x86-${version}.tar.bz2 && \
    mv /opt/murmur-static_x86-${version} /opt/murmur

USER murmur
WORKDIR /home/murmur

# Copy in our slightly tweaked INI
COPY murmur.ini /etc/murmur.ini

# Forward appropriate ports
EXPOSE 64738/tcp 64738/udp

# Read murmur.ini and murmur.sqlite from /data/
VOLUME ["/home/murmur"]

# Run murmur
ENTRYPOINT ["/opt/murmur/murmur.x86", "-fg", "-v"]
CMD ["-ini", "/etc/murmur.ini"]
