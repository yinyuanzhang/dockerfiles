FROM azul/zulu-openjdk-alpine:latest
WORKDIR /data
RUN apk update && \
    apk --no-cache add sqlite unzip && \
    wget https://repo.e-hentai.org/hath/HentaiAtHome_1.4.2.zip && \
    unzip HentaiAtHome_1.4.2.zip && \
    rm *.zip *.bat HentaiAtHomeGUI.jar && \
    apk del curl unzip

ENTRYPOINT ["java", "-jar", "HentaiAtHome.jar"]