# latest oracle openjdk is the basis
FROM openjdk:oracle

# set maintainer
MAINTAINER Murat Artim "muratartim@gmail.com"

# copy jar
COPY target/EquinoxExchangeServer-*.jar exchangeServer/exchangeServer.jar

# copy libraries
COPY target/libs exchangeServer/libs

# copy resources
COPY resources/config.properties exchangeServer/resources/config.properties

# expose server port
EXPOSE 1234

# change to server directory
WORKDIR /exchangeServer

# start server
CMD ["java", "-jar", "exchangeServer.jar", "-XX:+UseStringDeduplication", "-Xverify:none", "-server", "-XX:+UseParallelGC"]

# To build the docker image: (from where this file is located)
# docker image build -t muratartim/equinox_exchange_server:latest .

# To create & run the container:
# docker container run -e sftp.hostname=equinox_sftp_server 
#                      -e sftp.port=22 
#                      -e sftp.username=aurora 
#                      -e sftp.password=17891917 
#                      -e sftp.rootPath=filerRoot/ 
#                      -p 1234:1234 -d --name equinox_exchange_server --network equinox_network muratartim/equinox_exchange_server

# To start an existing container
# docker container start equinox_exchange_server