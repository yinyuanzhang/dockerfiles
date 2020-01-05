FROM nginx:1.17-alpine

LABEL maintainer="Boyd Lamers <b.lamers@eventstravel.com>"

ENV PROXY_REQUESTS_PER_SECOND_LIMIT 10
ENV PROXY_BURST 50
ENV PROXY_PASS_PROTOCOL https
ENV PROXY_PASS_HOST api.ipify.org/?format=json
ENV DNS_RESOLVER 1.1.1.1 1.0.0.1

ADD nginx.conf /etc/nginx/nginx-proxy.conf

ADD entry.sh /entry.sh

WORKDIR /

RUN ["chmod", "+x", "/entry.sh"]
CMD ["/entry.sh"]
