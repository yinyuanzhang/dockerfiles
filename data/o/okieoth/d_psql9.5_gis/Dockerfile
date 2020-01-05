FROM postgres:9.5
RUN apt-get update && apt-get install -y --force-yes postgresql-9.5-postgis-2.3

COPY scripts/import.sh /import.sh
COPY pgtune-0.9.3.tar.gz /opt

RUN cd /opt; tar -xzf pgtune-0.9.3.tar.gz; ln -s pgtune-0.9.3 pgtune

ENTRYPOINT ["/import.sh"]
CMD ["postgres"]



