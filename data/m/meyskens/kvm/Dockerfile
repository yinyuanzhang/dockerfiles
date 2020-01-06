FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
	iptables \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	libvirt-daemon-system \
	python-gi \
	python-ipaddr \
	qemu-kvm \
	virtinst \
	virt-viewer \
    virt-manager \
    iptables \
    qemu-utils \
    pulseaudio \
    net-tools \
    python-spice-client-gtk \
    gir1.2-spice-client-gtk-3.0 \
    wget \
	--no-install-recommends \
&& rm -rf /var/lib/apt/lists/*

RUN cd /root/ && wget https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso

COPY start.sh /root/start.sh

CMD /root/start.sh

