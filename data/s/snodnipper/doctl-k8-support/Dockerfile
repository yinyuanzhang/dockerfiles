FROM digitalocean/doctl

RUN apk add curl \
    && apk add python3 \
    && apk add openssl \
    && curl -L https://git.io/get_helm.sh | bash \
    && curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
    && chmod u+x kubectl    
