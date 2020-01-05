FROM alpine:3.9
RUN apk update && \
    apk add --no-cache curl

#add postgresql-client
RUN apk add --no-cache postgresql-client

#add mysql-client
RUN apk add --no-cache mysql-client

#add redis
RUN apk add --no-cache redis

#add kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod u+x kubectl && mv kubectl /usr/bin/kubectl

#add minio
RUN curl -LO https://dl.minio.io/client/mc/release/linux-amd64/mc && \
    chmod u+x mc && mv mc /usr/bin/mc

ADD version /usr/bin/version
RUN chmod +x /usr/bin/version