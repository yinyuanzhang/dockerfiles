
FROM scratch
ADD rootfs64.tar.gz /
ADD squashfs-tools.tar.gz /
ADD nodejs.tczs.tgz /

RUN mkdir -p /tmp/tce/optional \
    && chown -R root:staff /tmp/tce \
    && chmod -R g+w /tmp/tce \
    && $(cd etc/sysconfig; ln -s ../../tmp/tce tcedir) \
    && echo -n > etc/sysconfig/tcuser \
    && mkdir /home/tc \
    && chown tc:staff /home/tc \
    && su tc -c "cd /home && tce-load -ic nodejs-0.12.0.tcz" \
  	&& rm -f /home/nodejs-0.12.0.tcz \
  	&& rm -f /home/nodejs-0.12.0.tcz.dep \
  	&& rm -f /home/openssl-1.0.1.tcz \
    && chmod a+x /etc/profile.d/nodejs.sh

ENV PATH /usr/local/bin/nodejs/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV NODE_PATH /usr/local/bin/nodejs/lib/node_modules
USER tc
CMD ["/bin/sh"]
