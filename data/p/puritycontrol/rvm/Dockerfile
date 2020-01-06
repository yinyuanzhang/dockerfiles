FROM puritycontrol/ubuntu-dev:16.04

RUN apt-get update && apt-get install -y sudo libpq-dev curl \
  && gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 \
  && curl -L https://get.rvm.io | sudo /bin/bash -s stable \
  && /bin/bash -l -c "rvm requirements run" && rm -rf /var/lib/apt/lists/*


