FROM haproxy:1.5
MAINTAINER Orange Elpaaso Team <xx@orange.com>
COPY haproxy.cfg.template /usr/local/etc/haproxy/haproxy.cfg.template
COPY launch.sh /usr/local/etc/haproxy/launch.sh

RUN chmod ugo+x /usr/local/etc/haproxy/launch.sh

# CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
EXPOSE 80
EXPOSE 8080
CMD ["/usr/local/etc/haproxy/launch.sh"]