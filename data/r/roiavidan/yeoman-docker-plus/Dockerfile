FROM node:10-alpine

WORKDIR /app
RUN apk add --no-cache bash git openssh sudo

RUN yarn global add yo
RUN echo "node ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    chown node: /app && \
    mkdir -p /home/node/.ssh && chown node: /home/node/.ssh && \
    printf "#!/bin/sh\nsudo cp -p /root/.ssh/id_rsa /home/node/.ssh\nsudo chown node: /home/node/.ssh/id_rsa\nexec \"\$@\"\n" > /entrypoint.sh && \
    chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
USER node
