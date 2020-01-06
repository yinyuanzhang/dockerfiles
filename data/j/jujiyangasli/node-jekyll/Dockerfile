FROM debian:jessie

COPY ./init /usr/local/bin/init
COPY ./build /usr/local/bin/build

RUN apt update && apt install -y curl && curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt install -y nodejs netcat && gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 && curl -sSL https://get.rvm.io | bash -s stable --ruby --gems=jekyll

CMD [ "/bin/bash", "/usr/local/bin/init" ]
