FROM golang:1.10-alpine3.7

RUN apk --no-cache add wget git \
  && go get github.com/mholt/caddy \
  && go get github.com/caddyserver/builds \
  && cd src/github.com/mholt/caddy \
  && git -c advice.detachedHead=false checkout v0.11.0 \
  && cd caddy \
  && sed -i '/\/\/ This is where other plugins get plugged in (imported)/a \
\\t_ "github.com/nicolasazrak/caddy-cache" // http.cache\n \
\t_ "github.com/jung-kurt/caddy-cgi" // http.cgi\n \
\t_ "github.com/captncraig/cors" // http.cors\n \
\t_ "github.com/payintech/caddy-datadog" // http.datadog\n \
\t_ "github.com/linkonoid/caddy-dyndns" // dyndns\n \
\t_ "github.com/epicagency/caddy-expires" // http.expires\n \
\t_ "github.com/filebrowser/caddy/filemanager" // http.filemanager\n \
\t_ "github.com/echocat/caddy-filter" // http.filter\n \
\t_ "github.com/caddyserver/forwardproxy" // http.forwardproxy\n \
\t_ "github.com/kodnaplakal/caddy-geoip" // http.geoip\n \
\t_ "github.com/pyed/ipfilter" // http.ipfilter\n \
\t_ "github.com/BTBurke/caddy-jwt" // http.jwt\n \
\t_ "github.com/simia-tech/caddy-locale" // http.locale\n \
\t_ "github.com/tarent/loginsrv/caddy" // http.login\n \
\t_ "github.com/hacdias/caddy-minify" // http.minify\n \
\t_ "github.com/Xumeiquer/nobots" // http.nobots\n \
\t_ "github.com/miekg/caddy-prometheus" // http.prometheus\n \
\t_ "github.com/mastercactapus/caddy-proxyprotocol" // http.proxyprotocol\n \
\t_ "github.com/xuqingfeng/caddy-rate-limit" // http.ratelimit\n \
\t_ "github.com/captncraig/caddy-realip" // http.realip\n \
\t_ "github.com/freman/caddy-reauth" // http.reauth\n \
\t_ "github.com/hacdias/caddy-webdav" // http.webdav\n' \
    caddymain/run.go \
  && go get \
  && go run build.go \
  && ./caddy -version | head -n1 \
  && ./caddy -plugins

RUN mkdir -p /usr/share/GeoIp/ \
  && wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz \
  && tar -xzvf GeoLite2-City.tar.gz \
  && rm GeoLite2-City.tar.gz \
  && cd GeoLite2-City* \
  && cp GeoLite2-City.mmdb /usr/share/GeoIp \
  && cd .. && rm -rf GeoLite2-City*
# ---

FROM alpine:3.7

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/sithladyraven/docker-caddy" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0"

RUN apk --update --no-cache add ca-certificates

COPY --from=0 /usr/share/GeoIp/GeoLite2-City.mmdb /usr/share/GeoIp/
COPY --from=0 /go/src/github.com/mholt/caddy/caddy /usr/local/bin/
COPY ./Caddyfile /etc/caddy/
ENV CADDYPATH /var/lib/caddy

EXPOSE 80 443 2015

CMD ["caddy", "-conf", "/etc/caddy/Caddyfile", "--log", "stdout", "--agree=true"]
