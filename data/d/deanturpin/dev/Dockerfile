FROM ubuntu
RUN apt update --yes

# Install timezone package before keepass2
RUN apt install --yes tzdata
RUN apt install --yes keepass2
RUN apt install --yes iproute2
RUN apt install --yes docker.io
RUN apt install --yes iputils-ping
RUN apt install --yes clang-format
RUN apt install --yes chromium-browser
RUN apt install --yes iputils-tracepath

# Just the essentials
RUN apt install --yes man
RUN apt install --yes vim
RUN apt install --yes git
RUN apt install --yes make
RUN apt install --yes time
RUN apt install --yes curl
RUN apt install --yes g++-8
RUN apt install --yes tmux
RUN apt install --yes inotify-tools
RUN apt install --yes gpg
RUN apt install --yes tmux
RUN apt install --yes eog

# Configure build area
COPY . src
WORKDIR src

# Copy scripts and install bsah config
COPY bin/* /usr/bin/
RUN make
RUN mkdir /developer
COPY src/makefile /developer/
WORKDIR /developer
RUN rm -rf /src
