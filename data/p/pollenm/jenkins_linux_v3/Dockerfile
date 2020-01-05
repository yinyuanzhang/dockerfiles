#The MIT License
#
#  Copyright (c) 2015-2018, CloudBees, Inc. and other Jenkins contributors
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

FROM ubuntu:18.04
MAINTAINER Pollen Metrology <admin-team@pollen-metrology.com>

# https://docs.docker.com/get-started/part2/#build-the-app
# https://github.com/shufo/jenkins-slave-ubuntu/blob/master/Dockerfile
# https://github.com/jenkinsci/docker-slave
# https://github.com/jenkinsci/docker-jnlp-slave

ARG VERSION=3.28
ARG user=jenkins
ARG group=jenkins
ARG uid=2222

RUN apt-get clean
RUN apt update

# Install JDK latest edition
RUN apt install -y --no-install-recommends default-jdk

# Install utilities
RUN apt install -y git wget curl python-virtualenv python-pip build-essential python-dev zip \
	graphviz locales locales-all bind9-host iputils-ping sudo shellcheck python3-venv python3-pip

RUN pip3 install --system lcov_cobertura

RUN apt install -y libeigen3-dev libxt-dev libtiff-dev libpng-dev libjpeg-dev libopenblas-dev \
	xvfb libusb-dev

# QT5 conan package building dependencies
RUN apt install -y libgl1-mesa-dev libxcb1 libxcb1-dev \
libx11-xcb1 libx11-xcb-dev libxcb-keysyms1 libdbus-1-dev \
libxcb-keysyms1-dev libxcb-image0 libxcb-image0-dev libxtst-dev \
libxcb-shm0 libxcb-shm0-dev libxcb-icccm4 libxi-dev libminizip-dev \
libxcb-icccm4-dev libxcb-sync1 libxcb-sync-dev libxrandr-dev \
libxcb-xfixes0-dev libxrender-dev libxcb-shape0-dev libxml2-dev \
libxcb-randr0-dev libxcb-render-util0 libxcb-render-util0-dev \
libxcb-glx0-dev libxcb-xinerama0 libxcb-xinerama0-dev \
libfontconfig1-dev libxcomposite-dev libxcursor-dev libxslt1-dev \
libevent-dev libjsoncpp-dev protobuf-compiler libprotobuf-dev \
libvpx-dev libsnappy-dev libnss3-dev bison libbison-dev \
flex libfl-dev gperf libdbus-1-dev fontconfig libdrm-dev \
libxcomposite-dev libxcursor-dev libxi-dev libxrandr-dev \
xscreensaver libxtst-dev libegl1-mesa-dev

# VTK conan package building dependencies
RUN apt install -y freeglut3-dev mesa-common-dev mesa-utils-extra \
libgl1-mesa-dev libglapi-mesa libsm-dev libx11-dev libxext-dev \
libxt-dev libglu1-mesa-dev

# Install compilation utilities
RUN apt-get install -y software-properties-common gcc-7 g++-7 cmake lsb-core doxygen clang-format lcov gcovr valgrind && \
	update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 60 && \
	update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60

# Install node
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -y nodejs

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt update && apt install -y yarn

# Install chrome
RUN apt install -y chromium-browser
RUN update-alternatives --install /usr/bin/chrome chrome-browser /usr/bin/chromium-browser 100

# Add user jenkins to the image
RUN adduser --system --quiet --uid ${uid} --group --disabled-login ${user}

# Install and setup Conan
RUN python -m pip install --upgrade pip conan


# Install Phabricator-related tools
RUN DEBIAN_FRONTEND=noninteractive apt install -y php7.2-cli php7.2-curl
RUN mkdir -p /home/phabricator
RUN cd /home/phabricator && git clone https://github.com/phacility/arcanist.git
RUN cd /home/phabricator && git clone https://github.com/phacility/libphutil.git

# Linters
RUN cd /home/phabricator && git clone https://github.com/pinterest/arcanist-linters.git
RUN cd /home/phabricator && git clone https://github.com/vhbit/clang-format-linter.git

# Hack for multiplatform support of Phabricator Jenkins plugin
RUN mv /home/phabricator/arcanist/bin/arc.bat /home/phabricator/arcanist/bin/arc.bat.old
RUN ln -s /home/phabricator/arcanist/bin/arc /usr/bin/arc.bat


# Install last fresh cppcheck binary
RUN apt install -y libpcre3-dev unzip p7zip-full
RUN cd /tmp && mkdir cppcheck && wget https://github.com/danmar/cppcheck/archive/1.89.zip ;  \
	unzip -a 1.89.zip && \
	cd cppcheck-1.89 && \
	make -j4 MATCHCOMPILER=yes FILESDIR=/usr/bin/cfg HAVE_RULES=yes CXXFLAGS="-O2 -DNDEBUG -Wall -Wno-sign-compare -Wno-unused-function" && \
	make install PREFIX=/usr FILESDIR=/usr/share/cppcheck/ && \
	cd /tmp && \
	rm -rf cppcheck



RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

# USER jenkins
RUN echo "${user} ALL = NOPASSWD : /usr/bin/apt-get" >> /etc/sudoers.d/jenkins-can-install 

RUN mkdir -p /home/pollen && chown jenkins:jenkins /home/pollen && ln -s /home/pollen /pollen

# Create a folder for script and copy linux_cleaning into it
RUN mkdir -p /home/script && chown jenkins:jenkins /home/script
COPY linux_cleaning.sh /home/script
RUN chmod 755 /home/script/linux_cleaning.sh

# Create a folder for script and copy coverage_validator into it
RUN mkdir -p /home/script && chown jenkins:jenkins /home/script
COPY coverage_validator.sh /home/script

# If you put this label at the beginning of the Dockerfile, docker seems to use cache and build fails more often
LABEL Description="This is a base image, which provides the Jenkins agent executable (slave.jar)" Vendor="Jenkins project" Version="4.0"

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV JENKINS_AGENT_WORKDIR=${AGENT_WORKDIR}
ENV JENKINS_AGENT_NAME "NOT SET"
ENV JENKINS_SECRET "NOT SET"
ENV JENKINS_URL "NOT SET"


# Used to lauch automatically 
# the test version of Platypus
# on Bastion
RUN apt install -y daemonize

# Install merge-xml-coverage.py
RUN curl --create-dirs -sSLo /usr/bin/merge-xml-coverage.py https://gist.githubusercontent.com/tgsoverly/ef975d5b430fbce1eb33/raw/a4836655814bf09ac34bd42a6dd99f37aea7265d/merge-xml-coverage.py \
	&& chmod 755 /usr/bin/merge-xml-coverage.py

COPY jenkins-slave.sh /usr/bin/jenkins-slave.sh
RUN chmod +x /usr/bin/jenkins-slave.sh

# Install SonarQube stuff
#RUN curl --create-dirs -sSLo /tmp/build-wrapper-linux-x86.zip  https://xxxxx.xxxxx.xx:9000/static/cpp/build-wrapper-linux-x86.zip
# Use local copy to ensure wrapper matches server version
COPY build-wrapper-linux-x86.zip /tmp/build-wrapper-linux-x86.zip
RUN cd /home/jenkins && unzip -a /tmp/build-wrapper-linux-x86.zip

# Workaround, see https://community.sonarsource.com/t/sonarqube-c-ubuntu-build-wrapper-ld-preload-error/300/7
RUN ln -s /home/jenkins/build-wrapper-linux-x86/libinterceptor-x86_64.so /home/jenkins/build-wrapper-linux-x86/libinterceptor-haswell.so

RUN rm /tmp/build-wrapper-linux-x86.zip

RUN curl --create-dirs -sSLo /tmp/sonar-scanner-cli-3.3.0.1492-linux.zip \ 
	https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492-linux.zip
RUN cd /home/jenkins && unzip -a /tmp/sonar-scanner-cli-3.3.0.1492-linux.zip
RUN rm /tmp/sonar-scanner-cli-3.3.0.1492-linux.zip

ENTRYPOINT ["/usr/bin/jenkins-slave.sh"]
