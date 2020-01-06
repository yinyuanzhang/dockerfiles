FROM docker:latest

RUN apk update
RUN apk add python3 make mariadb-dev python3-dev gcc musl-dev curl libffi-dev libressl libressl-dev
RUN rm -rf /var/cache/apk/*

# install ecl-cli
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
RUN chmod +x /usr/local/bin/ecs-cli

RUN pip3 install --upgrade pip

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
