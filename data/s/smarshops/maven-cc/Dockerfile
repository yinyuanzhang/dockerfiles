FROM openjdk:8

RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.0.3.778-linux.zip && \
   unzip sonar-scanner-cli-3.0.3.778-linux.zip  && \
   cd /usr/bin && ln -s /sonar-scanner-3.0.3.778-linux/bin/sonar-scanner sonar-scanner

RUN apt-get update && apt-get install -y curl wget zip unzip git-all build-essential g++
RUN curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github&version=6.44.0" -o cf.tar.gz
RUN tar -xzvf cf.tar.gz
RUN mkdir -p /usr/local/bin
RUN mv cf /usr/local/bin
RUN curl -L "https://github.com/mikefarah/yq/releases/download/2.4.1/yq_linux_amd64" -o yq
RUN mv yq /usr/local/bin
RUN chmod +x /usr/local/bin/yq
COPY Gemfile .
COPY Gemfile.lock .
RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import -
RUN curl -sSL https://rvm.io/pkuczynski.asc | gpg --import -
RUN curl -sSL https://get.rvm.io | bash -s stable
ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN /bin/bash -l -c "rvm install 2.3.7"
RUN /bin/bash -l -c "gem install bundler"
RUN /bin/bash -l -c "bundle install"
RUN cf add-plugin-repo CF-Community https://plugins.cloudfoundry.org
RUN cf install-plugin blue-green-deploy -r CF-Community -f

USER root
RUN apt-get install -y ed jq postgresql openssl
