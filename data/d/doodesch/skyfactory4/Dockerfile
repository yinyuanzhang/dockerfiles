FROM openjdk:alpine
MAINTAINER Stefan Urban <stefan.urban@live.de>

USER root
WORKDIR /minecraft

VOLUME ["/minecraft/world"]
EXPOSE 25565

# Download and unzip minecraft files
RUN apk update && apk add curl wget && \
    mkdir -p /minecraft/world && \
    curl -LO https://media.forgecdn.net/files/2787/18/SkyFactory_4_Server_4.1.0.zip && \
    unzip SkyFactory_4_Server_4.1.0.zip && \
    rm SkyFactory_4_Server_4.1.0.zip && \
    mv ./SkyFactory_4_Server_4.1.0/* ./
    
# Accept EULA
RUN echo "# EULA accepted on $(date)" > /minecraft/eula.txt && \
    echo "eula=TRUE" >> eula.txt

# Install minecraft server itself
RUN /bin/sh /minecraft/Install.sh

# Startup script
CMD ["/bin/sh", "/minecraft/ServerStart.sh"] 
