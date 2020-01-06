FROM ubuntu:xenial

RUN apt-get -qq update
RUN apt -qqy upgrade
RUN apt-get -qq update

#install packages
RUN apt-get install -y xvfb curl \
  build-essential xvfb default-jre kmod git ssh-askpass openssh-client \
  python python-openssl zlib1g-dev software-properties-common firefox \
  libgconf2-4 libgtk2.0-0 libnotify-dev libnss3 libxss1 libasound2

# chromium-chromedriver chromium-browser

ENV DISPLAY :99.0

#JAVA repo
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java

# Trust google signing
RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN apt-get -qq update
RUN apt -qqy upgrade

RUN apt-get install -y nodejs google-chrome-stable oracle-java8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

#free up space
RUN rm -rf /var/lib/apt/lists/*

# give all users sudo
#RUN echo 'ALL ALL = (ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers


# Add the user UID:1000, GID:1000, home at /app
#RUN groupadd -r app -g 1000 && useradd -u 1000 -r -g app -m -d /app -s /sbin/nologin -c "App user" user1
#RUN chmod 755 /app

#RUN echo 'kernel.unprivileged_userns_clone=1' > /etc/sysctl.d/00-local-userns.conf
#RUN service procps restart

# Set the working directory to app home directory
#WORKDIR /app

#specify user to run commands as
#USER user1
