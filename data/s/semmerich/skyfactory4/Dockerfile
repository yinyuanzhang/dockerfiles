FROM openjdk:alpine
LABEL maintainer="sdemmer@widdletechinc.com"

ENV DOWNLOAD_LINK=https://media.forgecdn.net/files/2725/984
ENV VERSION=4.0.8
ENV JVM_OPTS="-Xms2048m -Xmx2048m"
USER root
WORKDIR /minecraft

VOLUME ["/minecraft/world"]
EXPOSE 25565

# Download and unzip minecraft files
RUN apk update && apk add curl wget && \
    mkdir -p /minecraft/world && \
    curl -LO ${DOWNLOAD_LINK}/SkyFactory_4_Server_${VERSION}.zip && \
    unzip SkyFactory_4_Server_${VERSION}.zip && \
    rm SkyFactory_4_Server_${VERSION}.zip
    
# Accept EULA
RUN echo "# EULA accepted on $(date)" > /minecraft/eula.txt && \
    echo "eula=TRUE" >> eula.txt

# Install minecraft server itself
RUN /bin/sh /minecraft/Install.sh

# Startup script
CMD ["/bin/sh", "/minecraft/ServerStart.sh"] 
