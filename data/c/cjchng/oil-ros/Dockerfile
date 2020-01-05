FROM ubuntu:14.04
MAINTAINER anto "m07158031@o365.mcut.edu.tw"
ENV DEBIAN_FRONTEND noninteractive

USER root
WORKDIR /root

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV locale-gen en_US.UTF-8
ENV dpkg-reconfigure locales

RUN apt-get update \
	&& apt-get install -qqy x11-apps \
	&& apt-get install -y --no-install-recommends \
		openssh-server \
		build-essential \
		gcc \
		xdg-utils \
 		nano \
		git \
		make \
		sudo \
		vim \
		unzip \
		curl \ 
		software-properties-common \
		pkg-config \
		python3-pip \
		python3-dev \
  		dbus-x11 \
		x11-xserver-utils \
		net-tools \
		man-db \
		xorg \
		xterm \
	&& apt-get autoremove -y \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& cd /usr/local/bin \
	&& ln -s /usr/bin/python3 python \
	&& pip3 install --upgrade pip \
	&& pip install --upgrade setuptools \
	&& sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' \
	&& apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 \
	&& apt-get update && sudo apt-get install dpkg \
	&& apt-get install -y ros-indigo-desktop-full


# Create user "Sudoer" with sudo powers
RUN useradd -m sudoer \
	&& usermod -aG sudo sudoer \
	&& echo '%sudo ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers \
	&& sudo usermod -s /bin/bash sudoer \
	&& cp /root/.bashrc /home/sudoer/ \
	&& chown -R --from=root sudoer /home/sudoer 

RUN sudo rosdep init \
	&& rosdep update 

WORKDIR /home/sudoer
ENV HOME /home/sudoer
ENV USER sudoer
USER sudoer
ENV PATH $HOME/.local/bin:$PATH

# Avoid first use of sudo warning.
RUN touch /home/sudoer/.sudo_as_admin_successful
RUN echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc

CMD [ "/bin/bash" ]
