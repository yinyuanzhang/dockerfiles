FROM minio/minio:RELEASE.2018-09-12T18-49-56Z

RUN apk add --update bash && rm -rf /var/cache/apk/*
# This is just so if we don't have rabbit_host specified it still works.
ENV RABBIT_HOST=www.google.com:80 

COPY wait-for-it.sh /usr/bin/wait-for-it.sh
RUN chmod +x /usr/bin/wait-for-it.sh

ENTRYPOINT /usr/bin/wait-for-it.sh $(echo $RABBIT_HOST) -t 60 -- /usr/bin/docker-entrypoint.sh server /export
