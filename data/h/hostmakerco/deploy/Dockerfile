FROM docker:latest

# Install kubectl deps + make
RUN apk --update add --no-cache git openssh make openssl curl tar gzip bash wget gnupg ca-certificates && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk && \
    apk add glibc-2.28-r0.apk && \
    rm glibc-2.28-r0.apk

# Install kubectl, kubesec and helm
COPY ./kubeconfig /root/.kube/config
ENV DESIRED_VERSION=v2.16.1
RUN curl -o- https://raw.githubusercontent.com/helm/helm/master/scripts/get | bash && \
    curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl && \
    curl -sSL https://github.com/shyiko/kubesec/releases/download/0.9.2/kubesec-0.9.2-linux-amd64 -o kubesec && \
    chmod a+x kubesec && mv kubesec /usr/local/bin/ && \
    curl -sSL https://github.com/shyiko/kubesec/releases/download/0.9.2/kubesec-0.9.2-linux-amd64.asc -o kubesec.asc && \
    curl -sS https://keybase.io/shyiko/pgp_keys.asc | gpg --import && \
    gpg --verify kubesec.asc /usr/local/bin/kubesec && \
    rm kubesec.asc && \
    wget -O /usr/bin/aws-iam-authenticator https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v0.4.0/aws-iam-authenticator_0.4.0_linux_amd64 && \
    chmod +x /usr/bin/aws-iam-authenticator && \
    chmod 600 /root/.kube/config && \
    chown root:root /root/.kube/config

# Install aws-cli
RUN apk add --no-cache python py-pip && \
    pip install --upgrade pip && \
    pip install awscli --user

ENV PATH=/root/.local/bin:$PATH
