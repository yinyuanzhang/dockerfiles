# Dockerfile for a Docker image providing OpenJDK 11, Maven and GitLab Runner.

FROM debian:latest
LABEL maintainer="p.st@wwu.de"

# Installing JDK 11 and Maven
RUN apt-get update -y \
    && apt-get install -y curl openjdk-11-jdk maven

# Installing Gitlab Runner
RUN curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | bash \
    && apt-get install -y gitlab-runner \
    && rm -rf /var/lib/apt/lists/*
