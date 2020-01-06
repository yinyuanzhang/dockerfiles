# Docker Pandoc - Dockerfile

# Mario Ban, 2018-12, based on https://kofler.info/ebooks/markdown_pandoc/

FROM haskell:8

LABEL version="1.3.0"
LABEL maintainer="Mario Ban <mario.ban@bluewin.ch>"

ENV DEFAULT_UID 1000
ENV DEFAULT_GID 1000

# Install additional packages
RUN apt-get update -y && \
    apt-get install -y -o Acquire::Retries=10 \
        --no-install-recommends \
      texlive-latex-recommended \
      texlive-latex-extra \
      texlive-fonts-recommended \
      texlive-fonts-extra \
      texlive-lang-german \
      texlive-pstricks \
      texlive-font-utils \
      lmodern \
      imagemagick \
      unzip \
      python3 \
      ghostscript \
      subversion \
      joe \
      vim \
      less \
      sudo \
      procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Aliases
RUN sed -i -e 's/# export LS_OPTIONS/export LS_OPTIONS/' -e 's/# alias/alias/' /root/.bashrc

# Set timezone CET (UTC+1)
# (see https://serverfault.com/questions/683605)
RUN cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime

# Install additional fonts for LaTeX
#ADD myfonts.tgz /usr/local/share/texmf
#RUN texhash

# Add user and group
RUN groupadd --gid $DEFAULT_GID docker && useradd --uid $DEFAULT_UID --create-home --no-log-init -g docker -G sudo docker

# No password for sudo
RUN echo "docker ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/010_docker-nopasswd
RUN chmod 440 /etc/sudoers.d/010_docker-nopasswd

# Set user to use
USER docker:docker

# Aliases
RUN sed -i -e 's/#force_color_prompt=yes/force_color_prompt=yes/' -e 's/#alias l/alias l/' /home/docker/.bashrc

# Docker Hub build problem: out of memory ...
ENV GHCRTS '-M2G'

# Install pandoc (current pandoc 2.9)
RUN cabal update && \
    cabal install pandoc

#RUN cabal new-update && \
#    cabal new-install pandoc pandoc-citeproc pandoc-crossref

ENV PATH /home/docker/.cabal/bin:$PATH

# Create and set working directory
WORKDIR /data

# Create mount point /data to hold an externally mounted volume
VOLUME ["/data"]

# Set the default command to run when starting the container
ENTRYPOINT ["/bin/bash"]

#ENTRYPOINT ["pandoc"]
#CMD ["--help"]
