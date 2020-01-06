FROM alpine:3.8

RUN apk --no-cache add --virtual .build-dependencies curl
RUN apk --no-cache add ca-certificates 

RUN curl -LO https://github.com/kubernetes/kops/releases/download/1.10.0/kops-linux-amd64
RUN chmod +x kops-linux-amd64
RUN mv kops-linux-amd64 /usr/local/bin/kops
RUN chmod +x /usr/local/bin/kops

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.12.3/bin/linux/amd64/kubectl
RUN mv kubectl /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl

RUN apk del --purge .build-dependencies
