FROM resin/rpi-raspbian:stretch
MAINTAINER RedZ

RUN sed -i 's|mirrordirector.raspbian.org|mirrors.ustc.edu.cn/raspbian|g' /etc/apt/sources.list \
&& sed -i 's|archive.raspbian.org|mirrors.ustc.edu.cn/raspbian|g' /etc/apt/sources.list \
&& sed -i 's|//archive.raspberrypi.org|//mirrors.ustc.edu.cn/archive.raspberrypi.org|g' /etc/apt/sources.list.d/raspi.list \
&& DEBIAN_FRONTEND=noninteractive apt-get update \
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils \
&& DEBIAN_FRONTEND=noninteractive apt-get -y upgrade \
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends sudo nano locales whois \
&& cp -f /etc/locale.alias /usr/share/locale/locale.alias \
&& sed -i "s/^#\ \+\(en_US.UTF-8\)/\1/" /etc/locale.gen \
&& locale-gen en_US en_US.UTF-8 \
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
cups printer-driver-foo2zjs printer-driver-fujixerox \
hpijs-ppds hp-ppd hplip samba

ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 LANGUAGE=en_US:en TZ=Asia/Shanghai

RUN useradd --groups=sudo,lp,lpadmin --create-home --home-dir=/home/pi --shell=/bin/bash --password=$(mkpasswd pi) pi \
&& sed -i '/%sudo[[:space:]]/ s/ALL[[:space:]]*$/NOPASSWD:ALL/' /etc/sudoers \
&& DEBIAN_FRONTEND=noninteractive apt-get -y autoremove \
&& DEBIAN_FRONTEND=noninteractive apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& mkdir /var/lib/apt/lists/partial \
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
&& echo $TZ > /etc/timezone

COPY cupsd.conf /etc/cups/cupsd.conf
EXPOSE 137/udp 138/udp 139 445 631
ADD setup.sh /root/
RUN chmod +x /root/setup.sh
CMD /root/setup.sh
