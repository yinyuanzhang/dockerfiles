FROM alpine

ENV PS1 "\n\n>> borg \W \$ "

RUN apk --no-cache add bash borgbackup openssh-client
RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh

WORKDIR /borg
VOLUME ["/root/.cache/borg", "/root/.config/borg", "/root/.ssh"]

ENTRYPOINT ["borg"]
