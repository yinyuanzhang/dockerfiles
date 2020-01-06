FROM shimjye/x2ubuntu-base
LABEL maintainer="shimjye@gmail.com"

# https://askubuntu.com/questions/854168/how-i-can-fix-appstream-cache-update-completed-but-some-metadata-was-ignored-d
RUN apt install -y appstream/xenial-backports
RUN appstreamcli refresh --force
RUN apt-get update

RUN add-apt-repository ppa:x2go/stable
RUN apt-get update
RUN apt-get install -y x2goserver x2goserver-xsession

RUN mkdir -p /home/dockerx/dockerinit/kr
RUN chown -R 1000:1000 /home/dockerx
ADD kr/profile /home/dockerx/dockerinit/kr/profile
ADD kr/environment /home/dockerx/dockerinit/kr/environment
ADD kr/fcitx-autostart.desktop /home/dockerx/dockerinit/kr/fcitx-autostart.desktop

EXPOSE 22

CMD ["/run.sh"]
