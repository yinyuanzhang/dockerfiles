FROM ikoobdevops/jenkins
MAINTAINER Blake Park  "blkpark@blkpark.com"

# needed by docker
USER root
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

USER jenkins