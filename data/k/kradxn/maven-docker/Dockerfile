FROM maven:3.6.0-ibmjava-8

RUN apt update && \
curl -sSL https://get.docker.com/ | sh && \
apt install -y curl ssh && \
curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
apt install -y nodejs zip && \
npm install -g --unsafe-perm --verbose @angular/cli && \
apt install -y python-pip && \
pip install awscli --upgrade --user && \
npm install -g cfn-create-or-update && \
apt-get autoremove -y
