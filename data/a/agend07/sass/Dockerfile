FROM debian:wheezy

RUN apt-get update

RUN apt-get install -y \
    rubygems \
    build-essential

RUN gem install sass

CMD cd /assets && sass --watch styles:css --poll --sourcemap=none
