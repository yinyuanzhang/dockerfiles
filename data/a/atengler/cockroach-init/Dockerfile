FROM cockroachdb/cockroach:latest

COPY ./entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
