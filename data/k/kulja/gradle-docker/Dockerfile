FROM java:8-jdk

# Gradle
ENV GRADLE_VERSION 2.14.1
ENV GRADLE_SHA cfc61eda71f2d12a572822644ce13d2919407595c2aec3e3566d2aab6f97ef39

RUN cd /usr/lib \
 && curl -fl https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o gradle-bin.zip \
 && echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c - \
 && unzip "gradle-bin.zip" \
 && ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \
 && rm "gradle-bin.zip"

# Set Appropriate Environmental Variables
ENV GRADLE_HOME /usr/lib/gradle
ENV PATH $PATH:$GRADLE_HOME/bin

# Timezone
RUN echo Europe/Zagreb > /etc/timezone

# Default command is "/usr/bin/gradle -version" on /usr/bin/app dir
# (ie. Mount project at /usr/bin/app "docker --rm -v /path/to/app:/usr/bin/app gradle <command>")
WORKDIR /usr/bin/app

CMD export JAVA_OPTS="-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=41256" && gradle bootRun > server.log
