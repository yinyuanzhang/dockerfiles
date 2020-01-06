FROM muicoder/jre

ENV ANDROID_HOME=/android
ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# Install Ant and Maven, Nodejs
RUN apk add --no-cache apache-ant maven nodejs-current-npm && \
    rm -rf /usr/lib/jvm/java-*-openjdk && \
    ln -sf $JAVA_HOME /usr/lib/jvm/default-jvm && \
    apk add --no-cache --virtual .build-dependencies python2-dev build-base && \
    npm install -g appium wd appium-doctor && \
    apk del --purge .build-dependencies && \
    cd ~ ; ls -A ~ | xargs -t rm -rf && \
    rm -rf /tmp/*

EXPOSE 4723

CMD ["appium"]
