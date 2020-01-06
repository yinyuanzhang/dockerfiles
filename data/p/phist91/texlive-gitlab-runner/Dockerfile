# Dockerfile for a Docker image providing a full up-to-date TeX Live
# installation with minted package support (and therefore with Python and
# Pygments) and pre-installed GitLab Runner.

FROM phist91/texlive-full-minted:latest
LABEL maintainer="p.st@wwu.de"

# Installing Gitlab Runner
RUN apt-get update -y \ 
    && apt-get install -y curl \
    && curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | bash \
    && apt-get install -y gitlab-runner
