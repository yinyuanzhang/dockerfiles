FROM postgres:9.3
#RUN localedef -i de_DE -c -f UTF-8 -A /usr/share/locale/locale.alias de_DE.UTF-8
#ENV LANG de_DE.utf8
RUN apt-get update && apt-get install -y --force-yes postgresql-9.3-postgis-2.1

COPY scripts/import.sh /import.sh
COPY pgtune-0.9.3.tar.gz /opt

RUN cd /opt; tar -xzf pgtune-0.9.3.tar.gz; ln -s pgtune-0.9.3 pgtune

ENTRYPOINT ["/import.sh"]
CMD ["postgres"]



