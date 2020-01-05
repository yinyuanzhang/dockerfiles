FROM debian:jessie
MAINTAINER Peter Etelej <peter@etelej.com>

RUN apt-get update && apt-get upgrade -y --no-install-recommends \
	&& apt-get install -y ca-certificates wget xz-utils libxrender1 libxt6 libxtst6 fontconfig \
	&& wget https://github.com/peteretelej/wkhtmltopdf-docker/releases/download/0.0.1/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
	&& tar -xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
	&& cp wkhtmltox/bin/* /usr/local/bin \
	&& rm -rf wkhtmltox* \
	&& apt-get purge -y --auto-remove wget xz-utils \
	&& rm -rf /var/lib/apt/lists/*

CMD ["wkhtmltopdf"]


  
