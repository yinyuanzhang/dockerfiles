FROM iwanbk/box-dev-ubuntu1804
MAINTAINER Iwan Budi Kusnanto <iwanbk@gmail.com>
RUN	cd && \
	wget -c https://dl.google.com/go/go1.11.2.linux-amd64.tar.gz && \
	tar zxf go1.11.2.linux-amd64.tar.gz && \

	# vim
	cd ~/.vim/bundle && \
	git clone https://github.com/fatih/vim-go.git

#env variables
ADD bashrc /tmp
RUN cat /tmp/bashrc >> ~/.bashrc
RUN rm /tmp/bashrc
