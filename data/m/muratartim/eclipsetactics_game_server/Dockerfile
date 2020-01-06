# latest oracle openjdk is the basis
FROM openjdk:oracle

# set maintainer
MAINTAINER Murat Artim "muratartim@gmail.com"

# copy jar
COPY target/EclipseTacticsServer-*.jar eclipseServer/eclipseServer.jar

# copy libraries
COPY target/libs eclipseServer/libs

# copy resources
COPY resources/properties.txt eclipseServer/resources/properties.txt

# expose server port
EXPOSE 1234

# change to server directory
WORKDIR /eclipseServer

# start server
CMD ["java", "-XX:+UseStringDeduplication", "-Xverify:none", "-server", "-XX:+UseParallelGC", "-jar", "eclipseServer.jar"]

# To build the docker image: (from where this file is located)
# docker image build -t muratartim/eclipsetactics_game_server:latest .

# To create & run the container:
# docker container run -e databaseHostname=eclipsetactics_sql_server 
#					   -e databasePort=1527 
#					   -e databasePath=/dbs 
#					   -e databaseUsername=val1 
#					   -e databasePassword=val2 
#					   -e uploadConnectionSettings=false
#					   -p 1234:1234 -d --name eclipsetactics_game_server --network eclipsetactics_network muratartim/eclipsetactics_game_server

# To start an existing container
# docker container start eclipsetactics_game_server