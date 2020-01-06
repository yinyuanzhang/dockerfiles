FROM dperson/samba

COPY ./entrypoint /entrypoint
RUN chmod +x /entrypoint
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint"]