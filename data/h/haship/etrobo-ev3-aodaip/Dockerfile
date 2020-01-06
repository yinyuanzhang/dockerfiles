FROM ubuntu

RUN set -x && apt-get update \
    && apt-get install -y \
    git \
    xz-utils \
    apt-utils software-properties-common \
    u-boot-tools \
    make g++ libboost-all-dev \
    wget curl unzip \
    language-pack-ja-base language-pack-ja

# locale
ENV LANG=ja_JP.UTF-8

# 作業用フォルダ
RUN mkdir /ev3rt
WORKDIR /ev3rt

# TOPPERS EV3RT スクリプトダウンロード
RUN wget http://ev3rt-git.github.io/public/ev3rt-prepare-ubuntu.sh

# スクリプト実行
RUN echo 1 | bash ev3rt-prepare-ubuntu.sh

ENV PATH $PATH:/opt/gcc-arm-none-eabi-6-2017-q1-update/bin

# TOPPERS/EV3RT の設定
#RUN wget http://www.toppers.jp/download.cgi/ev3rt-beta7-3-release.zip
COPY ev3rt-beta7-3-release.zip /ev3rt
RUN unzip ev3rt-beta7-3-release.zip \
    && tar Jxvf ev3rt-beta7-3-release/hrp2.tar.xz

# cfg
WORKDIR /ev3rt/hrp2/cfg
RUN make

# 設定変更
WORKDIR /ev3rt/hrp2/sdk/common
RUN echo "APPL_DIR += \$(foreach dir,\$(shell find \$(APPLDIR) -type d),\$(dir))" >> Makefile.prj.common

# sample program
WORKDIR /ev3rt
RUN wget https://github.com/ETrobocon/etroboEV3/archive/master.zip && unzip master.zip
WORKDIR  etroboEV3-master/SampleCode/EV3way_EV3RT_sample
RUN cp -r sample_c4 /ev3rt/hrp2/sdk/workspace/

# useradd etrobo
RUN mkdir /home/etrobo \
    && useradd -d /home/etrobo etrobo \
    && chown -R etrobo:etrobo /ev3rt/hrp2/ \
    && chown -R etrobo:etrobo /home/etrobo/
USER etrobo

WORKDIR /ev3rt/hrp2/sdk/workspace
