FROM docker:stable-git

RUN apk add --no-cache curl bash ca-certificates jq python py-pip

RUN pip install -U pip && pip install awscli \
    && curl -SL https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl > /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && curl -SL https://github.com/istio/istio/releases/download/0.8.0/istio-0.8.0-linux.tar.gz | tar xzf - -C /tmp/ \
    && mv /tmp/istio-0.8.0/bin/istioctl /usr/local/bin/istioctl \
    && chmod +x /usr/local/bin/istioctl \
    && rm -rf /tmp/*
