FROM alpine:latest

RUN apk add bash curl
RUN curl https://getcaddy.com | bash -s personal dns,dyndns,http.awslambda,http.cache,http.cgi,http.cors,http.expires,http.geoip,http.git,http.jwt,http.minify,http.nobots,http.ratelimit,http.s3browser,http.webdav,tls.dns.cloudflare,tls.dns.digitalocean,tls.dns.dyn,tls.dns.linode,tls.dns.ovh,tls.dns.route53,tls.dns.vultr

WORKDIR /etc/caddy
VOLUME [ "/etc/caddy" ]

ENTRYPOINT ["caddy", "-agree"]