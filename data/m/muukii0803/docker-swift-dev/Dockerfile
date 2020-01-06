FROM swift:3.1.0

MAINTAINER Muukii <m@muukii.me>

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV ON_DOCKER YES

RUN apt-get -q update
RUN apt-get install -y \
	git \
	wget \
	curl \
	zsh \
	vim \
	tmux
    
RUN git clone https://github.com/muukii/env.dotfiles.git /env.dotfiles
WORKDIR /env.dotfiles
RUN make

WORKDIR /

# Define default command.
CMD ["/bin/zsh"]

