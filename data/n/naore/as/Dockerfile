FROM ubuntu:latest as pv_builder

RUN apt-get update \
 && apt-get install curl -y \
 && curl -L -o /tmp/go.sh https://install.direct/go.sh \
 && chmod +x /tmp/go.sh \
 && /tmp/go.sh

FROM shadowsocks/shadowsocks-libev:latest as ss_builder

FROM alpine

LABEL maintainer=naore

RUN uname -a

# ss-4

COPY --from=ss_builder /usr/bin/ss-* /usr/bin/
RUN apk add --no-cache rng-tools \
      $(scanelf --needed --nobanner /usr/bin/ss-* \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u)
COPY s.json /etc/shadowsocks-libev/config.json
COPY s.pid /s.pid

# pv-2

COPY --from=pv_builder /usr/bin/v2ray/* /usr/bin/v2ray/
#COPY --from=pv_builder /usr/bin/v2ray/v2ray /usr/bin/v2ray/
#COPY --from=pv_builder /usr/bin/v2ray/v2ctl /usr/bin/v2ray/
#COPY --from=pv_builder /usr/bin/v2ray/geoip.dat /usr/bin/v2ray/
#COPY --from=pv_builder /usr/bin/v2ray/geosite.dat /usr/bin/v2ray/
COPY v.json /etc/v2ray/config.json

RUN apk --no-cache add ca-certificates && \
    mkdir /var/log/v2ray/ &&\
    chmod +x /usr/bin/v2ray/v2ctl && \
    chmod +x /usr/bin/v2ray/v2ray
    
# sshd-0

RUN apk add --no-cache --update openssh sed \
        && rm -rf /var/cache/apk/* /tmp/*  \
	&& mkdir -p /root/.ssh \
        && mkdir /var/run/sshd \
        && echo 'root:admin' |chpasswd \
        && sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
	&& sed -i "s/#PasswordAuthentication.*/PasswordAuthentication yes/" /etc/ssh/sshd_config \
#        && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \
        && sed -ri 's/^#?Port .*/Port 16100/' /etc/ssh/sshd_config \
	&& ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key \
	&& ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key \
	&& ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key 

# Complete

RUN apk add --no-cache --update supervisor \
    && rm -rf /var/cache/apk/* /tmp/* \
    && mkdir /var/log/supervisor
COPY supervisord.conf /etc/supervisord.conf

EXPOSE 16100 16102 16103 16104

ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf"]
