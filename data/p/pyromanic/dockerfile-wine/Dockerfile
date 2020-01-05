FROM	pyromanic/debian-s6
RUN	dpkg --add-architecture i386
RUN 	apt-get update && 	\
	apt-get install 	\
		sudo		\
		wine		\
		wine32		\
		xterm		\
	 -y && \
	apt-get clean

RUN	useradd user
RUN	mkdir /home/user
RUN	chown user /home/user
RUN	echo "user	ALL=(ALL)NOPASSWD:ALL " >> /etc/sudoers
RUN	echo "" >> /etc/sudoers
CMD 	sudo -u user wine cmd
