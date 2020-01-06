FROM audkar/docker-android-sdk

# npm
RUN apk --update add npm bash coreutils

# gradle
RUN wget -q -O gradle.zip "https://services.gradle.org/distributions/gradle-4.9-bin.zip"
RUN unzip gradle.zip
RUN mv "gradle-4.9" "/opt/gradle/"
RUN rm gradle.zip
RUN ln -s "/opt/gradle/bin/gradle" /usr/bin/gradle
RUN addgroup -S -g 1100 gradle
RUN adduser -D -S -G gradle -u 1100 -s /bin/ash gradle
RUN mkdir /home/gradle/.gradle
RUN export GRADLE_USER_HOME=/home/gradle/.gradle
RUN chown -R gradle:gradle /home/gradle
ENV PATH "${PATH}:/opt/gradle/bin"
