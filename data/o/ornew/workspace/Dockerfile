FROM ubuntu:xenial

RUN apt-get update \
 && apt-get install -y \
      sudo git make build-essential \
      libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils \
      tk-dev libxml2-dev libxmlsec1-dev libffi-dev

ENV WORKSPACE /workspace
ENV HOME $WORKSPACE

RUN groupadd -g 1000 workspace \
 && useradd -g workspace -G sudo -u 1000 -d $WORKSPACE -s /bin/bash workspace \
 && mkdir -m 755 -p $WORKSPACE \
 && chown workspace:workspace $WORKSPACE \
 && echo 'workspace ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER workspace:workspace
WORKDIR $HOME

ENV DEFAULT_PYTHON_VERSION 3.6.6

COPY ./bin $WORKSPACE/bin
RUN sudo chown -R workspace:workspace $WORKSPACE/bin \
 && $WORKSPACE/bin/workspace_setup

EXPOSE 8888

ENTRYPOINT ["/bin/bash","/workspace/bin/workspace"]
