FROM centos:7

ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/bin/dumb-init
RUN chmod +x /usr/bin/dumb-init

RUN yum update -y && \
    yum install -y ca-certificates wget vim nano git

RUN curl -s https://packages.gitlab.com/install/repositories/runner/gitlab-ci-multi-runner/script.rpm.sh | bash && \
    yum install -y gitlab-ci-multi-runner && \
    wget https://github.com/docker/machine/releases/download/v0.8.2/docker-machine-Linux-x86_64 -O /usr/bin/docker-machine && \
    chmod +x /usr/bin/docker-machine && \
    mkdir -p /etc/gitlab-runner/certs && \
    chmod -R 700 /etc/gitlab-runner


ADD entrypoint /
RUN chmod +x /entrypoint

# Update certs
RUN /usr/bin/update-ca-trust enable
RUN /usr/bin/update-ca-trust

VOLUME ["/etc/gitlab-runner", "/home/gitlab-runner"]
ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]
