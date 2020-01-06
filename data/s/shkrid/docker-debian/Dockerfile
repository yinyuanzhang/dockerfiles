FROM debian:jessie
MAINTAINER Shkrid <shkrid@gmail.com>

RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
		apache2 \
		bash-completion \
		python \
		vim \
	&& rm -rf /var/lib/apt/lists/*

#Uncoment compeltion section
RUN sed -i '/^#if ! shopt -oq posix; then$/,/^#fi$/ s/^#//' /etc/bash.bashrc

ENV VERSION 0.1
ENV TEXT 123

EXPOSE 80/udp 443

COPY Dockerfile /tmp/$TEXT.txt

#Run when container start 'docker run -it name'
#CMD ["/bin/bash"] from upstream image
#CMD ["/usr/bin/vi"]
#CMD ["apache2","-DFOREGROUND"]
#CMD echo $TEXT
#CMD cat /tmp/$TEXT.txt

ENTRYPOINT ["/bin/bash"]
CMD ["--help"]