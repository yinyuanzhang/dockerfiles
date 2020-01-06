FROM adoptopenjdk/openjdk8-openj9:alpine

LABEL maintainer.name="fivesmallq"
LABEL maintainer.email="fivesmallq@gmail.com"

RUN apk add --no-cache \
    unzip \
    wget \
    curl \
    zip \ 
    python \
    tzdata \
    openssh
    
# Timezone
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir -p /app

# ENV PLAY_VERSION __PLAY_VERSION__
ENV PLAY_VERSION="1.4.4"

RUN curl --location -s https://downloads.typesafe.com/play/${PLAY_VERSION}/play-${PLAY_VERSION}.zip > /tmp/play-${PLAY_VERSION}.zip \
      && unzip -q /tmp/play-${PLAY_VERSION}.zip -d /opt \
      && rm -rf /tmp/play-${PLAY_VERSION}.zip \
            /opt/play-${PLAY_VERSION}/COPYING \
            /opt/play-${PLAY_VERSION}/documentation \
            /opt/play-${PLAY_VERSION}/framework/test \
            /opt/play-${PLAY_VERSION}/play.bat \
            /opt/play-${PLAY_VERSION}/python/*.dll \
            /opt/play-${PLAY_VERSION}/python/python.* \
            /opt/play-${PLAY_VERSION}/README.textile \
            /opt/play-${PLAY_VERSION}/samples \
            /opt/play-${PLAY_VERSION}/support

RUN rm -fr /var/cache/apk/*

ENV PATH /opt/play-${PLAY_VERSION}:$PATH

WORKDIR /app

# EXPOSE 9000

CMD ["play"]
