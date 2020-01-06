FROM jenkins/jenkins:lts-slim

USER root

RUN apt-get update && \
    apt-get install -y automake autoconf build-essential libreadline-dev libncurses-dev libssl-dev libyaml-dev libxslt-dev libffi-dev libtool unixodbc-dev jq && \
    rm -rf /var/lib/apt/lists/*

USER jenkins

ENV JENKINS_HOME=/var/jenkins_home
ENV JENKINS_TEMP_HOME=/usr/share/jenkins/ref
ENV PATH="${PATH}:${JENKINS_HOME}/.asdf/shims:${JENKINS_HOME}/.asdf/bin:${JENKINS_TEMP_HOME}/.asdf/shims:${JENKINS_TEMP_HOME}/.asdf/bin"

RUN git clone --branch v0.5.0 https://github.com/asdf-vm/asdf.git $JENKINS_TEMP_HOME/.asdf && \
    echo '. $HOME/.asdf/asdf.sh' >> $JENKINS_TEMP_HOME/.bashrc && \
    echo '. $HOME/.asdf/asdf.sh' >> $JENKINS_TEMP_HOME/.profile

RUN asdf plugin-add python && \
    echo "python miniconda2-latest" >> $JENKINS_TEMP_HOME/.tool-versions && \
    echo "python miniconda3-latest" >> $JENKINS_TEMP_HOME/.tool-versions && \
    cd $JENKINS_TEMP_HOME && \
    asdf install
