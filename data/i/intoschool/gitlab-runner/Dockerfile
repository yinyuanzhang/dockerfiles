FROM gitlab/gitlab-runner
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install systemd -y
RUN apt-get remove docker docker-engine docker.io
RUN apt-get install docker.io -y
VOLUME ["/var/run/docker.sock", "/var/run/docker.sock"]
ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]