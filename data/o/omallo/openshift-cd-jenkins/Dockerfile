FROM openshift/jenkins-2-centos7:latest

USER 0

COPY ./contrib/bin /usr/local/bin

RUN curl --fail -L -o /usr/local/bin/gotpl https://github.com/omallo/gotpl/releases/download/v0.4.0/gotpl_linux_amd64 && \
    chmod 0755 /usr/local/bin/gotpl

USER 1001
