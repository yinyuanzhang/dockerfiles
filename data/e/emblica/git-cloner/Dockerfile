FROM alpine

RUN apk --update add openssh-client git
RUN adduser -D -u 1000 git && mkdir -p /mnt/git
WORKDIR /opt/git
RUN chown git:git /opt/git && chown git:git /mnt/git
USER 1000
COPY git.sh .

CMD /opt/git/git.sh
