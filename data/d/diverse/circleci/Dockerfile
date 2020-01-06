FROM docker:18.09-git

RUN apk add --no-cache python groff jq less bash && \
    apk add --no-cache --virtual .build-deps py-pip curl && \
    pip install --no-cache-dir awscli && \
    curl https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy | tee /usr/bin/ecs-deploy && \
    chmod +x /usr/bin/ecs-deploy && \
    apk del .build-deps \

