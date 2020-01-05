FROM alpine

LABEL MAINTAINER iLemonrain <ilemonrain@ilemonrain.com>

ENV SYS_APK_REPO="dl-cdn.alpinelinux.org"

ENV ocserv_username="vpnuser" \
    ocserv_userpass="vpnuser"

ENV ocserv_max_clients="8" \
    ocserv_max_same_client="2" \
    ocserv_tcp_port="6666" \
    ocserv_udp_port="6666" \
    ocserv_try_mtu_discovery="true" \
    ocserv_dns="8.8.8.8" \
    ocserv_cisco_client_compat="true"

# 系统核心升级
RUN ( sed -i "s/dl-cdn.alpinelinux.org/${SYS_APK_REPO}/g" /etc/apk/repositories ;\
      sed -i "s/dl-cdn.alpinelinux.org/${SYS_APK_REPO}/g" /etc/apk/repositories ;\ 
      apk --no-cache upgrade )

# 系统基础组件安装
RUN ( apk --no-cache add curl )

# 编译组件安装
RUN ( apk --no-cache add g++ make )

# Ocserv必需编译组件安装
RUN ( apk --no-cache add nettle-dev gnutls-dev protobuf-c-dev libev-dev talloc-dev \
      linux-pam-dev readline-dev http-parser-dev lz4-dev geoip-dev libseccomp-dev \
      libnl3-dev krb5-dev freeradius-client-dev gnutls-utils )

# 导入Ocserv源码
COPY src/ocserv-src.tar.xz /tmp/ocserv-src.tar.xz

# 编译安装Ocserv
RUN ( cd /tmp/ ;\
      tar xf ocserv-src.tar.xz ;\
      cd ocserv-0.12.0 ;\
      ./configure && make && make install ;\ 
      mkdir -p /etc/ocserv/ ;\ 
      cp doc/sample.config /etc/ocserv/ocserv.conf ;\
      cd / ;\
      rm -rf /tmp/ocserv-0.12.0/ )

# 生成自签发证书 (用于测试以及简易部署)
RUN ( ocserv_server_ip="$(curl -s whatismyip.akamai.com)" ;\
      cd /etc/ocserv ;\ 
      mkdir _tmp_selfcert ;\
      cd _tmp_selfcert ;\
      echo "cn = "Openconnect VPN Server - CA"" >> ca.tmpl ;\
      echo "organization = "Openconnect VPN Server"" >> ca.tmpl ;\
      echo "serial = 1" >> ca.tmpl ;\
      echo "expiration_days = 3650" >> ca.tmpl ;\
      echo "ca" >> ca.tmpl ;\
      echo "signing_key" >> ca.tmpl ;\
      echo "cert_signing_key" >> ca.tmpl ;\
      echo "crl_signing_key" >> ca.tmpl ;\ 
      certtool --generate-privkey --outfile ca-key.pem ;\
      certtool --generate-self-signed --load-privkey ca-key.pem \
            --template ca.tmpl --outfile ca-cert.pem ;\
      echo "cn = "${ocserv_server_ip}"" >> server.tmpl ;\
      echo "organization = "Openconnect VPN Server"" >> server.tmpl ;\
      echo "expiration_days = 3650" >> server.tmpl ;\
      echo "signing_key" >> server.tmpl ;\
      echo "encryption_key" >> server.tmpl ;\
      echo "tls_www_server" >> server.tmpl ;\
      certtool --generate-privkey --outfile server-key.pem ;\
      certtool --generate-certificate --load-privkey server-key.pem --load-ca-certificate \
            ca-cert.pem --load-ca-privkey ca-key.pem --template server.tmpl --outfile \
             server-cert.pem ;\
      mkdir -p /etc/ocserv/certs/ ;\
      cp ca-cert.pem /etc/ocserv/certs/ca-cert.pem ;\
      cp server-cert.pem /etc/ocserv/certs/server-cert.pem ;\
      cp server-key.pem /etc/ocserv/certs/server-key.pem ;\
      cd / ;\
      rm -rf /etc/ocserv/_tmp_selfcert )

# 配置文件将在启动时动态生成并使用 (/etc/ocserv/ocserv.conf)

# 导入entrypoint.sh
COPY scripts/entrypoint.sh /usr/sbin/entrypoint.sh

# 导入no-route规则表
COPY src/cn-no-route.txt /etc/ocserv/cn-no-route.txt

EXPOSE 443

CMD [ "sh", "/usr/sbin/entrypoint.sh" ]