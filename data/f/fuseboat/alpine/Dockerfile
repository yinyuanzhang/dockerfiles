# Version Alpine
ARG IMAGE="alpine"
ARG VERSION=3.11

FROM $IMAGE:$VERSION

LABEL description="Image Base to alpine" \
    alpine="Alpine daily" \
    maintainer="Fusengine <info@fusengine.ch>"

# Default Config
ARG ALPINE_VERSION_REPOS=latest
ARG TIMEZONE="Europe/Zurich"
ARG ROOT_DIR="/root/.script_base/"

# create repository to script
RUN mkdir -p $ROOT_DIR
RUN chmod 777 $ROOT_DIR

# Add build pack script alpine
COPY scripts_base/ $ROOT_DIR
RUN chmod +x $ROOT_DIR*

# Run script
RUN .$ROOT_DIR/build.sh

# add zsh Bash
RUN sed -i -e "s/bin\/ash/bin\/zsh/" /etc/passwd

# Run Shell
ENV SHELL /bin/zsh

# RUN ZSH
CMD [ "zsh",  "--version"]
