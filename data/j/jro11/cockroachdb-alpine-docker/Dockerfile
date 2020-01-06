FROM alpine
RUN wget -qO- https://binaries.cockroachdb.com/cockroach-latest.linux-musl-amd64.tgz | tar  xvz

ENV COCKROACH_CHANNEL=official-docker

ENV COCKROACH_SECURE=false
# If running in secure mode, uncomment the following lines
#COPY certs certs
#ENV COCKROACH_SECURE=true

RUN cp cockroach-latest.linux-musl-amd64/cockroach /usr/local/bin/cockroach

COPY run.sh run.sh

RUN apk add bash

EXPOSE 26257 8080

CMD [ "/bin/bash","-c","./run.sh" ]