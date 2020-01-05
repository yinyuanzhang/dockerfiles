# Latest is fine for now
# hadolint ignore=DL3007
FROM cloudbees/cloudbees-jenkins-distribution:latest

# install docker as root
USER root
RUN curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh get-docker.sh

# Reset user to default
USER cloudbees-jenkins-distribution
