FROM alpine:3.8

ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 2222
COPY entrypoint /

RUN apk add --no-cache openssh \
  && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
  && echo "root:root" | chpasswd
