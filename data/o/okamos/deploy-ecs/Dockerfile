FROM docker:18.06.1-ce-git

RUN apk add --no-chace \
  bash jq python3 && \
  pip3 install awscli==1.16.22 && \
  wget -q https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy -O /usr/bin/ecs-deploy && \
  chmod +x /usr/bin/ecs-deploy
