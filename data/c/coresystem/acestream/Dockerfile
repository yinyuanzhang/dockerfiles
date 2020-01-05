FROM ubuntu:18.10
WORKDIR /tmp

# ACE Stream
# http://wiki.acestream.org/wiki/index.php/Download#Linux
COPY acestream_3.1.49_ubuntu_18.04_x86_64.tar.gz .
COPY acestream.conf .
RUN apt-get update -y && apt-get install -y --no-install-recommends curl net-tools libssl1.0.0 libpython2.7 \
	python-setuptools python-minimal python-pkg-resources python-m2crypto python-apsw python-lxml python-pkg-resources python-libxslt1 \
    && mkdir -p /opt/acestream \
    && tar -zxvf acestream_3.1.49_ubuntu_18.04_x86_64.tar.gz -C /opt/acestream \
	&& ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0 /opt/acestream/lib/libcrypto.so.1.0.0 \
    && ln -s /usr/lib/x86_64-linux-gnu/libssl.so.1.0.0 /opt/acestream/lib/libssl.so.1.0.0 \
    && chmod +x /opt/acestream/start-engine \
	&& cat acestream.conf > /opt/acestream/acestream.conf \
    && rm -rf /tmp/*
	
# set /tmp on tmpfs
RUN sed -i '$atmpfs /tmp tmpfs defaults,noatime,nosuid,nodev,noexec,mode=1777 0 0' /etc/fstab && \
	sed -i '$atmpfs /var/tmp tmpfs defaults,noatime,nosuid,nodev,noexec,mode=1777 0 0' /etc/fstab 

# add services
ADD start.sh /start.sh
RUN chmod +x /start.sh
WORKDIR /
