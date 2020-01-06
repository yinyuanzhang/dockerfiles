# Centos Ready for use Angular.js, Grunt, Bower, Yo, generator-angular
FROM centos

MAINTAINER Julien LENNE <contact.lenne@gmail.com>

# Add Epel
RUN yum install epel-release -y && \
	yum install openssl-devel gcc ruby ruby-devel tar bzip2 libpng-devel make git sudo  -y

# Clone NVM, define stable version of Node.js
RUN git clone https://github.com/creationix/nvm.git /.nvm
RUN echo ". /.nvm/nvm.sh" >> /etc/bash.bashrc

# NVM for all users
RUN /bin/bash -c '. /.nvm/nvm.sh && nvm install 0.10.34 && nvm alias default 0.10.34 && ln -s /.nvm/v0.10.34/bin/node /usr/bin/node && ln -s /.nvm/v0.10.34/bin/npm /usr/bin/npm'

# Update NPM
RUN /.nvm/v0.10.34/bin/npm install npm -g

# NPM Global
RUN npm install -g yo bower grunt-cli && \
    npm install -g generator-angular

# Add dev user to use npm, grunt, yeoman and bower + sudo
RUN useradd -r dev -d /home/dev && \
  echo "dev ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Create user directory and change owner
RUN mkdir /home/dev && chown -R dev:dev /home/dev


# set HOME so 'npm install' and 'bower install' don't write to /
ENV HOME /home/dev

# set utf8
ENV LANG en_US.UTF-8

# Create working directory
RUN mkdir /opt/src && chown dev:dev /opt/src
RUN /bin/bash -c 'gem install compass --no-ri --no-rdoc'

# Change current user (root) to dev
USER dev
# Modules Node.js in home/dev
WORKDIR /home/dev

# Use CDN because Installation fails with Error: read ECONNRESET or Error: connect ETIMEDOUT
# Auto correct npm set strict-ssl false
ENV PHANTOMJS_CDNURL http://cnpmjs.org/downloads
RUN npm install grunt grunt-contrib-imagemin phantomjs

# Change to working directory when the container start
WORKDIR /opt/src

VOLUME ["/opt/src"]
# Expose the port
EXPOSE 9000