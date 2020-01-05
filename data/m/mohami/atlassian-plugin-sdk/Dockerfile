FROM openjdk:8-jdk
MAINTAINER "Mohammed Davoodi" <support@mohami.io>

WORKDIR /opt

RUN apt-get update && \
sh -c 'echo "deb https://packages.atlassian.com/atlassian-sdk-deb stable contrib" >>/etc/apt/sources.list' && \
sh -c 'echo "deb http://security.ubuntu.com/ubuntu bionic-security main" >>/etc/apt/sources.list' && \
sh -c 'echo "deb http://in.archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse" >>/etc/apt/sources.list' && \
wget https://packages.atlassian.com/api/gpg/key/public  && \
apt-key add public && \
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32 && \
apt-get install -y --no-install-recommends apt-transport-https && \
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
apt-get install -y --no-install-recommends atlassian-plugin-sdk nodejs python-pip python-dev wget maven && \
pip install wheel && \
pip install --upgrade setuptools && \
pip install awscli --ignore-installed six && \
apt-get remove -y python-pip && \
rm -rf /var/lib/apt/lists/*

# Downloading gcloud package
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

# Installing the package
RUN mkdir -p /usr/local/gcloud \
  && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
  && /usr/local/gcloud/google-cloud-sdk/install.sh

# Adding the package path to local
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

CMD atlas-version && node -v && aws --version && gcloud --version
