FROM balenalib/aarch64-alpine
ADD https://raw.githubusercontent.com/sj8023ld/openwrt-test/master/openwrt.tar.gz /

EXPOSE 80

USER root

# using exec format so that /sbin/init is proc 1 (see procd docs)
CMD ["/sbin/init"]
