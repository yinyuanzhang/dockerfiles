FROM centos:7 AS build

ENV URLISO https://mirror.yandex.ru/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1810.iso
ENV URLFREEDOS http://www.fdos.org/bootdisks/ISO/FDOEMCD.builder.zip

# create PXE files
RUN curl $URLISO -o CentOS-7-x86_64-Minimal.iso
RUN yum install bsdtar syslinux -y
RUN bsdtar xfp CentOS-7-x86_64-Minimal.iso -C /mnt
RUN mkdir /opt/pxe/centos7 -p
RUN cp -r /mnt/repodata /opt/pxe/centos7
RUN cp -r /mnt/Packages /opt/pxe/centos7
RUN cp -r /mnt/LiveOS /opt/pxe/centos7
RUN cp /mnt/.treeinfo /opt/pxe/centos7
RUN mkdir /opt/pxe/boot/ -p
RUN cp /mnt/images/pxeboot/initrd.img /opt/pxe/boot/
RUN cp /mnt/images/pxeboot/vmlinuz /opt/pxe/boot/
RUN cp /usr/share/syslinux/pxelinux.0 /opt/pxe/boot/
RUN cp /usr/share/syslinux/vesamenu.c32 /opt/pxe/boot/
RUN cp /usr/share/syslinux/mboot.c32 /opt/pxe/boot/
RUN cp /usr/share/syslinux/chain.c32 /opt/pxe/boot/
RUN cp /usr/share/syslinux/memdisk /opt/pxe/boot/

# create FreeDOS iso. And copy flash files for bios
RUN yum install genisoimage unzip -y
RUN curl $URLFREEDOS -o FDOEMCD.builder.zip
RUN unzip FDOEMCD.builder.zip
COPY bios/ FDOEMCD/CDROOT
RUN mkdir /opt/pxe/boot/iso/ -p
RUN cd FDOEMCD && genisoimage -o /opt/pxe/boot/iso/freedos.img -b isolinux/isolinux.bin -no-emul-boot -boot-load-size 4 -boot-info-table -N -J -r \-c boot.catalog -hide boot.catalog -hide-joliet boot.catalog CDROOT

FROM centos:7
RUN yum install epel-release -y && yum install dnsmasq nginx -y && yum clean all && rm -rf /var/cache/yum

COPY --from=build /opt/pxe /mnt

COPY conf/nginx.conf /etc/nginx/conf.d/default.conf
COPY conf/boot.menu.cfg /mnt/boot/menu.cfg
COPY conf/pxelinux.cfg.default /mnt/boot/pxelinux.cfg/default
COPY conf/boots/* /mnt/boot/pxelinux.cfg/
COPY conf/servers/* /mnt/centos7/

COPY bin/nginx.run /nginx.run
COPY bin/dnsmasq.run /dnsmasq.run
COPY bin/run.run /run.run

EXPOSE 67 67/udp \
       69 69/udp \
       53 53/udp \
       80 80/tcp

ENTRYPOINT ["/run.run"]
