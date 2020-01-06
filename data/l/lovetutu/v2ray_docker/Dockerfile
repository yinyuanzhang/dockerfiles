FROM ubuntu:16.04
LABEL maintainer="Hackxiu <hackxiu@gmail.com>"

ENV Tim="Asia/Shanghai"
ENV CLIENT_ID "23ad6b10-8d1a-40f7-8ad0-e3e35cd38297"
ENV CLIENT_ALTERID 100
ENV CLIENT_WSPATH "/fuckgfw_letscrossgfw"
ENV VER="4.21.3"

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget sed net-tools gdebi network-manager network-manager-pptp network-manager-openvpn network-manager-vpnc unzip daemon tzdata vim

RUN wget --max-redirect=5 --no-check-certificate -O v2ray.zip https://github.com/v2ray/v2ray-core/releases/download/v$VER/v2ray-linux-64.zip \
    && mkdir ./v2ray \
	&& unzip -o -d ./v2ray v2ray.zip \
	&& mv ./v2ray/v2ray /usr/local/bin/ \
	&& mv ./v2ray/v2ctl /usr/local/bin/ \
	&& mv ./v2ray/geosite.dat /usr/local/bin/ \
	&& mv ./v2ray/geoip.dat /usr/local/bin/ \
	&& chmod 777 /usr/local/bin/v2ctl \
	&& chmod 777 /usr/local/bin/v2ray \
	&& chmod 777 /usr/local/bin/geosite.dat \
	&& chmod 777 /usr/local/bin/geoip.dat \
	&& rm -rf v2ray.zip \
	&& rm -rf v2ray

RUN mkdir /var/log/v2ray \
    && echo ${Tim} > /etc/timezone \
	&& mkdir /etc/v2ray \
	&& chmod -R 777 /var/log/v2ray \
	&& chmod -R 777 /etc/v2ray \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/cache/apt/*

ADD config.json /etc/v2ray/
ENV PATH /usr/local/bin:$PATH

RUN sed -i "s/CLIENT_ID/$CLIENT_ID/g" /etc/v2ray/config.json \
    && sed -i "s/CLIENT_ALTERID/$CLIENT_ALTERID/g" /etc/v2ray/config.json \
	&& sed -i "s#CLIENT_WSPATH#$CLIENT_WSPATH#g" /etc/v2ray/config.json

EXPOSE 8080

CMD ["v2ray", "-config=/etc/v2ray/config.json"]
