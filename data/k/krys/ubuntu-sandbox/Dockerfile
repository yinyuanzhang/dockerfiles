FROM krys/ubuntu-puppet-base

# Install some useful software package.
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
		command-not-found \
		zsh \
		apt-file \
		psmisc \
		iputils-ping \
		most \
		man-db \
		vim \
		wget \
		ca-certificates \
		git \
		mercurial \
		subversion

# Install "dialog" frontend for interactive apt-get calls
# (gets rid of the "No usable dialog-like program is installed" errors)
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends whiptail

# Update "apt-file" index
RUN apt-file update

RUN sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -) || exit 0"

COPY files /

RUN /puppet-apply.sh site.pp

CMD [ "zsh" ]

