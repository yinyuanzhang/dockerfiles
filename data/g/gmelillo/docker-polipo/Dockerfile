FROM ubuntu:18.04
MAINTAINER Gabriel Melillo <gabriel@melillo.me>

RUN apt-get update && apt-get install -y polipo && \
	echo 'proxyAddress = "0.0.0.0"' > /etc/polipo/config && \
	echo 'socksParentProxy = "tor:9050"' >> /etc/polipo/config && \
	echo 'socksProxyType = socks5' >> /etc/polipo/config

EXPOSE 8123
ENTRYPOINT ["polipo"]
CMD []
