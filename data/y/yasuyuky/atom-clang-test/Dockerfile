FROM circleci/node:13.5.0
MAINTAINER yasuyuky <yasuyuki.ymd@gmail.com>

USER root
RUN apt-get -y update && apt-get --assume-yes --quiet install curl libxss1 libx11-xcb1 libasound2 xvfb clang

CMD ["bash"]
