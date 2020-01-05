FROM alpine/git:1.0.7

ENV ACCESS_TOKEN=$ACCESS_TOKEN REPO=$REPO

ADD clone.sh /clone.sh
RUN chmod 755 /clone.sh
ENTRYPOINT [ "/bin/sh","/clone.sh"]