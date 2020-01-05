FROM docker:stable

RUN apk add --no-cache curl jq python py-pip yarn nodejs git
RUN pip install --upgrade pip
RUN pip install awscli docker-compose ecs-deploy urllib3==1.21.1
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest && \
		chmod +x /usr/local/bin/ecs-cli
