FROM alpine:3.9
COPY brook /
RUN chmod u+x /brook \
    && echo '/brook server -l :${PORT} -p ${PASSWORD}' >/start.sh
ENTRYPOINT ["/bin/sh", "/start.sh"]
