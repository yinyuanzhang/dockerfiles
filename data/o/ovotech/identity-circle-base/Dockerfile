FROM circleci/openjdk:8-jdk

RUN sudo apt-get update
RUN sudo apt-get install -y python-pip coreutils jq
RUN sudo pip install awscli
RUN sudo apt-get clean autoclean
RUN sudo apt-get autoremove --yes
RUN sudo rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN sudo curl -o /usr/local/bin/amm https://github.com/lihaoyi/Ammonite/releases/download/1.8.2/2.13-1.8.2 && \
    sudo chmod +x /usr/local/bin/amm

RUN sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest && \
    sudo chmod +x /usr/local/bin/ecs-cli

RUN wget -O /tmp/terraform.zip https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_linux_amd64.zip
RUN sudo unzip /tmp/terraform.zip -d /usr/local/bin && rm /tmp/terraform.zip
