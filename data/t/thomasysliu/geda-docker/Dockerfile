# Pull base image.
FROM ubuntu:18.10

# docker build --build-arg UID=$(id -u) --build-arg GID=$(id -g) -f Dockerfile -t gedatest .

ARG UNAME=developer
ARG UID=1000
ARG GID=1000
ARG UHOME=/home/$UNAME
ENV LANG zh_TW.UTF-8
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

# Install.
RUN apt-get clean && apt-get update && \
  apt-get install -y pcb geda gerbv geda-utils && \
  apt-get install -y pylint3 python3-pip && \
  pip3 install -U pip python-pptx pillow && \
  rm -rf /var/lib/apt/lists/*

USER $UNAME
# Set environment variables.
ENV HOME $UHOME

# Define working directory.
WORKDIR $UHOME

# Define default command.
CMD ["bash"]
  



