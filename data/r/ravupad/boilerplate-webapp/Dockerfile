FROM ubuntu:18.04
RUN apt update && \
    apt install -y curl gnupg && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt install -y nodejs && \
    npm i -g @angular/cli@6.2.3 && \
    curl https://download.java.net/java/GA/jdk10/10.0.2/19aef61b38124481863b1413dce1855f/13/openjdk-10.0.2_linux-x64_bin.tar.gz \
        --output openjdk-10.0.2_linux-x64_bin.tar.gz && \
    tar xzvf openjdk-10.0.2_linux-x64_bin.tar.gz && \
    update-alternatives --install /usr/bin/java java /jdk-10.0.2/bin/java 1 && \
    update-alternatives --install /usr/bin/javac javac /jdk-10.0.2/bin/javac 1
WORKDIR /app
COPY client/package.json client/package-lock.json client/
RUN cd client && npm i 
COPY server/build.gradle server/gradle.properties server/gradlew server/
COPY server/gradle/ server/gradle/
RUN cd server && ./gradlew build -x generateMainJooqSchemaSource --info
COPY client/ client/
RUN cd client && \
    ng build --prod && \
    mkdir -p ../server/src/main/resources/client && \
    cp -r dist/client/* ../server/src/main/resources/client/
COPY server/ server/
RUN cd server && ./gradlew build -x generateMainJooqSchemaSource --info
EXPOSE 8080
CMD cd server && java -jar -Dbemused_env=${BEMUSED_ENV} ./build/libs/server-0.0.1-fat.jar
