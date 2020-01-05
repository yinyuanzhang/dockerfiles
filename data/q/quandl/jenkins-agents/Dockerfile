# Dockerfile for image quandl/jenkins-slave:ruby
FROM jenkins/jnlp-slave

USER "root"

RUN apt-get update
RUN apt-get install -y --force-yes build-essential curl git ruby libpq-dev
RUN apt-get install -y --force-yes zlib1g-dev libssl-dev libreadline-dev libyaml-dev libxml2-dev libxslt-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN python -m pip install --upgrade awscli

# Install nodejs and npm
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs

# Copy package.json and .npmrc files to the container.
# The package.json file is a copy of the file of the same name in the quandl/next repository.
# The .npmrc file is needed to install/download the fortawesome dependencies.
COPY package.json /home/jenkins/package.json
COPY .npmrc /home/jenkins/.npmrc
WORKDIR /home/jenkins
RUN npm install

RUN apt-get clean

# Install rbenv and ruby-build
RUN git clone https://github.com/rbenv/rbenv.git /home/jenkins/.rbenv
RUN git clone https://github.com/rbenv/ruby-build.git /home/jenkins/.rbenv/plugins/ruby-build
RUN /home/jenkins/.rbenv/plugins/ruby-build/install.sh
ENV PATH /home/jenkins/.rbenv/bin:$PATH
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile

# Install multiple versions of ruby
# Add to the versions.txt file the ruby versions you want to install
ENV CONFIGURE_OPTS --disable-install-doc
ADD ./versions.txt /home/jenkins/versions.txt
RUN chown -R jenkins:jenkins /home/jenkins

USER "jenkins"
RUN xargs -L 1 rbenv install < /home/jenkins/versions.txt


# Install Bundler for each version of ruby
RUN eval "$(rbenv init -)"
RUN for v in $(cat /home/jenkins/versions.txt); do rbenv global $v; eval "$(rbenv init -)"; gem install bundler; done

ENV PATH /home/jenkins/.rbenv/shims:$PATH
ADD ./.gemrc /home/jenkins/.gemrc
