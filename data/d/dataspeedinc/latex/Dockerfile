FROM ubuntu:bionic

# AWS APT mirrors
RUN sed -i 's+http://security.ubuntu.com/+http://archive.ubuntu.com/+g' /etc/apt/sources.list \
 && sed -i 's+http://archive.ubuntu.com/+http://us-east-1.ec2.archive.ubuntu.com/+g' /etc/apt/sources.list \
 && apt update \
 && rm -rf /var/lib/apt/lists/*

# Install git and ssh
RUN apt update \
 && apt install -y git ssh-client \
 && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN apt update \
 && apt install -y --no-install-recommends \
        texlive-latex-base texlive-latex-extra texlive-fonts-recommended \
        texlive-latex-recommended texlive-extra-utils texlive-generic-extra poppler-utils \
        lmodern make tree \
 && rm -rf /var/lib/apt/lists/*

# Add LaTeX build script
ADD latex-build-all /usr/bin
