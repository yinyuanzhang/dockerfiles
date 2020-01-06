FROM gocd/gocd-agent-centos-7:v18.6.0

COPY ./assets/gcloud.repo /etc/yum.repos.d/

RUN yum install -y epel-release

RUN rpm -U http://opensource.wandisco.com/centos/7/git/x86_64/wandisco-git-release-7-2.noarch.rpm && \
    yum upgrade -y && \
    echo "Installing Gcloud" && \
    yum install -y git wget google-cloud-sdk which && \
    yum clean all && \
    rm -rf /var/cache/yum

RUN echo "Installing Terraform"  && \
    wget https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip && \
    unzip /terraform_0.11.7_linux_amd64.zip && \
    mv /terraform /usr/bin/. && \
    chmod 775 /usr/bin/terraform && \
    rm -f /terraform_0.11.7_linux_amd64.zip

RUN echo "Installing helm" && \
    curl -q https://storage.googleapis.com/kubernetes-helm/helm-v2.9.0-linux-amd64.tar.gz > helm.tar.gz && \
    tar xzf helm.tar.gz && \
    rm -rf helm.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/ && \
    chmod u+x /usr/local/bin/helm && \
    rm -rf linux-amd64 && \
    wget -O - https://github.com/roboll/helmfile/releases/download/v0.40.1/helmfile_linux_amd64 > helmfile_linux_amd64 && \
    mv helmfile_linux_amd64 /usr/local/bin/helmfile && \
    chmod +x /usr/local/bin/helmfile && \
    rm -rf helmfile_linux_amd64

ENV HELM_BIN=/usr/local/bin/helm \
    HELM_PLUGIN_DIR=/home/go/.helm

RUN echo "Installing helm" && \
    yum install -y kubectl

RUN echo "Installing Lint tools" && \
    yum install -y yamllint

RUN su - go -c "/usr/local/bin/helm init --client-only && \
                /usr/local/bin/helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable && \
                /usr/local/bin/helm repo add svc-cat https://svc-catalog-charts.storage.googleapis.com && \
                export PATH='$PATH:/usr/local/bin/:HELM_BIN=/usr/local/bin/:HELM_PLUGIN_DIR=/home/go/.helm/' && \
                helm plugin install https://github.com/lrills/helm-unittest"
