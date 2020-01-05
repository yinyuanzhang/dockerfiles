FROM python:3-stretch

# Install.
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get -y install build-essential curl ruby ruby-dev libxml2-dev libsqlite3-dev libxslt1-dev libpq-dev zlib1g-dev wget nfs-common cifs-utils smbclient && \
  gem install bosh_cli --no-ri --no-rdoc && \
  wget -O cfcli.tgz "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" && \
  tar -xvzf cfcli.tgz && \
  chmod 755 cf && \
  mv cf /usr/bin && \
  wget -O jq "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64" && \
  chmod 755 ./jq && \
  mv ./jq /usr/bin && \
  apt-get -y install git && \
  apt-get -y install sshpass

# Add concourse python modules
RUN \
  pip3 install git+https://github.com/lorands/concourse-python-tooling.git

RUN pip3 install --upgrade awscli cloudfoundry-client

CMD ["/bin/bash"]