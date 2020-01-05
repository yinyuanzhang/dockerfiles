FROM docker:dind

RUN apk add --no-cache openssh-client git
RUN eval $(ssh-agent -s)
RUN mkdir -p ~/.ssh
RUN chmod 700 ~/.ssh
RUN touch ~/.ssh/known_hosts
RUN chmod 644 ~/.ssh/known_hosts
