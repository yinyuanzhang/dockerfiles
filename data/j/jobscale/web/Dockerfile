FROM nginx
SHELL ["bash", "-c"]
WORKDIR /var/site
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y vim git unzip curl \
 tmux zip openssh-client net-tools dnsutils iputils-ping procps
COPY . projects/_
COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf
RUN rm -fr /etc/nginx/site* /etc/nginx/conf.d \
 && mkdir /var/site/web \
 && ln -sfn /var/site/projects/_/etc/nginx/conf.d /etc/nginx/conf.d \
 && ln -sfn /var/site/projects/_/site/error /var/site/web/error
RUN ln -sfn tls ssl \
 && . projects/_/ssl-keygen \
 && mkdir tls \
 && mv sslGen/wildcard.jsx.jp.cert tls/cert.pem \
 && mv sslGen/wildcard.jsx.jp.key tls/cert.key \
 && openssl dhparam 256 > tls/dhparam.pem
RUN rm -fr /var/lib/apt/lists/*
EXPOSE 80 443
CMD ["bash", "-c", ". projects/_/cmd"]
