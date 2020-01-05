# mianor64/xclient
# http://stackoverflow.com/questions/2150882/how-to-automatically-add-user-account-and-password-with-a-bash-script
# echo thePassword | passwd theUsername --stdin
# echo -e "password\npassword\n" | passwd ## Ubuntu 13.04


FROM ubuntu:14.04
MAINTAINER Bob <mianor64@gmail.com>

# first create user and group for all the X Window stuff
# required to do this first so we have consistent uid/gid between server and client container
RUN addgroup --system xusers \
  && adduser \
			--home /home/xclient \
			--disabled-password \
			--shell /bin/bash \
			--gecos "user for running an xclient application" \
			--ingroup xusers \
			--quiet \
			xclient \
  && echo 'xclient:xclient' | chpasswd
 
#
RUN usermod -aG sudo xclient

# Install packages required for connecting against X Server
RUN apt-get update && apt-get install -y --no-install-recommends \
				xauth \
		&& rm -rf /var/lib/apt/lists/*

# Before switching user, root needs to ensure that entrypoint can be executed.
COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# During startup we need to prepare connection to X11-Server container
USER xclient
ENTRYPOINT ["/entrypoint.sh"]