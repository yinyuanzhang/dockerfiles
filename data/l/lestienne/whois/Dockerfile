FROM debian:stretch-20190708 as whois-builder

ENV WHOIS_VERSION=5.4.2~bpo9+1

RUN echo deb http://http.debian.net/debian stretch-backports main contrib non-free | \ 
    tee /etc/apt/sources.list.d/stretch-backports.list && \
    apt-get update -qq && apt-get install -y whois=$WHOIS_VERSION

# RUN readelf -d /usr/bin/whois  | grep 'NEEDED'

FROM gcr.io/distroless/base

COPY --from=whois-builder /usr/bin/whois /usr/bin/whois
COPY --from=whois-builder ["/lib/x86_64-linux-gnu/libc*", \
         "/lib/x86_64-linux-gnu/libidn*", \
         "/lib/x86_64-linux-gnu/"]

ENTRYPOINT ["whois"]
CMD ["--help"]