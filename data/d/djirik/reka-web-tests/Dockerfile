FROM ubuntu:16.04
# Install Java 8


RUN set -x \
    && apt-get update \
    && apt-get install -y \
        ca-certificates-java \
        openjdk-8-jre \
        openjdk-8-jre \
        openjdk-8-jdk \
        openjdk-8-jdk \
        curl \
        wget

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME


# Install node 8
RUN set -x &&\
    curl -sL https://deb.nodesource.com/setup_10.x | bash - &&\
    apt-get install -y nodejs

# Install Chrome

RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/chrome.list

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN set -x \
    && apt-get update \
    && apt-get install -y \
        xvfb \
        google-chrome-stable

ADD scripts/xvfb-chrome /usr/bin/xvfb-chrome
RUN ln -sf /usr/bin/xvfb-chrome /usr/bin/google-chrome

ENV CHROME_BIN /usr/bin/google-chrome

# # Install firefox

# RUN set -x \
#     && apt-get update \
#     && apt-get install -y \
#         pkg-mozilla-archive-keyring


# RUN set -x \
#     && apt-get update \
#     && apt-get install -y \
#         xvfb \
#     && apt-get install -y \
#         firefox-esr

# ADD scripts/xvfb-firefox /usr/bin/xvfb-firefox
# RUN ln -sf /usr/bin/xvfb-firefox /usr/bin/firefox

# ENV FIREFOX_BIN /usr/bin/firefox

# This is needed for PhantomJS
RUN set -x && \
    apt-get update && \
    apt-get install -y \
        bzip2 \
        zip

# RUN node -v
# RUN npm -v
# RUN yarn -v
# RUN java -version
# RUN mvn -v
# RUN apt-cache policy firef
