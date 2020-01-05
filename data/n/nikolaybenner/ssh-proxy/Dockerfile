FROM alpine:3.2

RUN apk add --update openssh-client && rm -rf /var/cache/apk/*
CMD rm -rf /root/.ssh && mkdir /root/.ssh && cp -R /root/ssh/* /root/.ssh/ && chmod -R 600 /root/.ssh/* && \
ssh -o StrictHostKeyChecking=no -NL *:$LOCAL_PORT:localhost:$REMOTE_PORT  $REMOTE_USER@$REMOTE_HOST
#&& while true; do sleep 30; done;
EXPOSE 1-65535