FROM alpine:latest

RUN apk add --update nodejs yarn python3 git && \
    # upgrade pip to the latest version to get rid of the warning
    pip3 install --upgrade pip

RUN pip3 install awscli --upgrade --user

RUN yarn global add serverless
