FROM absolutapps/oracle-12c-ee-base

ENV INIT_MEM_PST 40
ENV SW_ONLY false
ENV TERM dumb

ADD entrypoint.sh /entrypoint.sh

EXPOSE 1521
EXPOSE 8080
EXPOSE 5500

VOLUME ["/u01/app/oracle"]

ENTRYPOINT ["/entrypoint.sh"]

