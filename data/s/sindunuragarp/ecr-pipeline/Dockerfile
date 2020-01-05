FROM node:8-alpine

# https://github.com/mesosphere/aws-cli/blob/master/Dockerfile
RUN apk -v --update add python py-pip groff less mailcap && \
    pip install --upgrade awscli==1.14.5 s3cmd==2.0.1 python-magic && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*

# prepare wb npm
RUN npm install -g npx npm-login-cmd && \
    npm config set registry https://npm.widgetbrain.io