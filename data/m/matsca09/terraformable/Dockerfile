FROM ubuntu:18.04
RUN apt-get update && \
	apt install -y wget unzip python python-pip openssh-client && \
	apt clean && rm -rf /var/lib/apt/lists/*
RUN wget -O /tmp/terraform.zip https://releases.hashicorp.com/terraform/0.11.13/terraform_0.11.13_linux_amd64.zip && \
	unzip /tmp/terraform.zip -d /usr/local/bin/ && \
	chmod +x /usr/local/bin/terraform && \
	rm /tmp/terraform.zip
RUN wget -O /usr/local/bin/sentry-cli https://github.com/getsentry/sentry-cli/releases/download/1.47.1/sentry-cli-Linux-x86_64 && chmod +x /usr/local/bin/sentry-cli
RUN pip install ansible>2.7 && rm -rf /root/.cache
WORKDIR /root
