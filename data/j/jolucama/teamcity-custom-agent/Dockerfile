FROM jetbrains/teamcity-agent:latest

MAINTAINER Jose Luis Cardosa <jlcardosa@gmail.com>

RUN apt-get update \
 && unset JAVA_TOOL_OPTIONS \
 && echo "unset JAVA_TOOL_OPTIONS" >> ~/.bashrc \
 && apt-get install -y openjdk-11-jdk \
 && export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64/bin" \
 && echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/bin" >> ~/.bashrc \
 && curl -O https://bootstrap.pypa.io/get-pip.py \
 && python get-pip.py --user \
 && echo "export PATH=~/.local/bin:$JAVA_HOME:$PATH" >> ~/.bashrc \
 && ~/.local/bin/pip install awscli --upgrade --user \
 && apt-get install -y apt-transport-https \
 && curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - \
 && echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list \
 && apt-get update \
 && apt-get install -y kubectl \
 && mkdir .kube \
 && curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.12.7/2019-03-27/bin/linux/amd64/aws-iam-authenticator \
 && chmod +x ./aws-iam-authenticator \
 && mv ./aws-iam-authenticator /usr/local/bin/aws-iam-authenticator \
 && curl -O https://storage.googleapis.com/kubernetes-helm/helm-v2.13.1-linux-amd64.tar.gz \
 && tar -zxvf helm-v2.13.1-linux-amd64.tar.gz \
 && cp linux-amd64/helm /usr/local/bin/helm \
 && curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh \
 && bash nodesource_setup.sh \
 && apt-get install -y nodejs
