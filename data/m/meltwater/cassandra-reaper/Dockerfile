FROM thelastpickle/cassandra-reaper:1.3.0

# Install secretary
RUN wget -O /usr/bin/secretary "https://github.com/meltwater/secretary/releases/download/0.10.1/secretary-`uname -s`-`uname -m`" && \
    chmod +x /usr/bin/secretary && \
    echo "d0b31c48ede726b8700fda88e7c0d5c13b353a0d  /usr/bin/secretary" | sha1sum -c -

COPY launch.sh /launch.sh
ADD configure-persistence.sh /usr/local/bin/configure-persistence.sh

RUN chown reaper:reaper \
        /usr/local/bin/configure-persistence.sh && \
    chmod u+x \
        /usr/local/bin/configure-persistence.sh

ENTRYPOINT ["/launch.sh"]
CMD ["cassandra-reaper"]