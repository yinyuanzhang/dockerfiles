FROM ubuntu:18.04

# unattended installation of packages
ENV DEBIAN_FRONTEND noninteractive

# install linux oracle instant client
RUN mkdir /opt/oracle

# install linux instantclient deps
COPY --from=mafs/instantclient:mafsgo  /linux-instantclient /opt/oracle

RUN ln -s /opt/oracle/instantclient_12_2/libclntsh.so.12.1 /opt/oracle/instantclient_12_2/libclntsh.so

ENV NLS_LANG AMERICAN_AMERICA.US7ASCII
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_12_2

# install windows oracle instant client (for cross compiling)
RUN mkdir /usr/lib/oracle

# install windows instantclient deps
COPY --from=mafs/instantclient:mafsgo  /windows-instantclient /usr/lib/oracle

# set pkg_config_path
ENV PKG_CONFIG_PATH "${GOPATH}/pkgconfig"
COPY pkgconfig ${GOPATH}/pkgconfig

# install system updates and setup some utilities
RUN apt-get update &&\
    apt-get install -y \
        software-properties-common \
        build-essential \
        jq \
        vim \
        zip \
        unzip \
        libaio1 \
        zlib1g-dev \
        curl \
        pkg-config \
        openssh-client \
        gcc-mingw-w64 \
        python \
        python-pip \
        shellcheck

# install latest version of git
RUN add-apt-repository ppa:git-core/ppa &&\
    apt-get update &&\
    apt-get install -y \
        git

# install go & add to path
RUN curl -L -o /usr/local/go1.12.3.linux-amd64.tar.gz https://dl.google.com/go/go1.12.3.linux-amd64.tar.gz &&\
    tar -C /usr/local -xzf /usr/local/go1.12.3.linux-amd64.tar.gz
ENV GOPATH /root/go
ENV PATH "${PATH}:/usr/local/go/bin:${GOPATH}/bin"

# download & install terraform
RUN LATEST_TERRAFORM_VER=$(curl -s https://checkpoint-api.hashicorp.com/v1/check/terraform | jq -r -M '.current_version') &&\
    curl -L -o terraform.zip https://releases.hashicorp.com/terraform/${LATEST_TERRAFORM_VER}/terraform_${LATEST_TERRAFORM_VER}_linux_amd64.zip &&\
    unzip terraform.zip &&\
    mv terraform /usr/local/bin/

# download & install tflint
RUN LATEST_TFLINT_VER=$(curl -H 'Accept: application/json' -L -X GET -s "https://github.com/wata727/tflint/releases/latest" | jq -c --raw-output '.tag_name') &&\
    curl -L -o tflint.zip https://github.com/wata727/tflint/releases/download/${LATEST_TFLINT_VER}/tflint_linux_amd64.zip &&\
    unzip tflint.zip &&\
    mv tflint /usr/local/bin/

# AWS cli
RUN pip install awscli

# niceties
RUN chmod -x /usr/bin/dircolors &&\
    echo "syntax off" > /root/.vimrc &&\
    echo "alias ll='ls -alF'" >> /root/.bashrc

# add github.com to known_hosts
RUN mkdir ~/.ssh/ &&\
    ssh-keyscan -H github.com >> ~/.ssh/known_hosts

# cleanup after package installs
RUN apt-get clean

# install go packages
WORKDIR ${GOPATH}

CMD [ "bash" ]
