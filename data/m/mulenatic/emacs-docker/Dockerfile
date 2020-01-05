# Use the newest emacs version from silex as base
FROM silex/emacs
RUN apt-get update; apt-get install -y python git sudo; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;
COPY ["emacs.el", "/home/docker/.emacs.el"]
COPY ["startup.sh", "/home/docker"]
COPY ["Cask", "/home/docker/.emacs.d/Cask"]
# Add a non-root user
RUN useradd -m -d /home/docker -s /bin/bash docker; \
	adduser docker sudo; \
	echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers; \
	chown -R docker /home/docker;
USER docker
ENV git.email="mulenatic@gmail.com" \
	git.user="Thomas Kaczmarek" \
	PATH="/home/docker/.cask/bin:$PATH" \
	TERM=xterm-256color
RUN   git config --global user.email $git.user; git config --global user.name $git.user; \
	curl -fsSL https://raw.githubusercontent.com/cask/cask/master/go | python; \
	cd /home/docker/.emacs.d; cask install
ENTRYPOINT ["/home/docker/startup.sh"]
