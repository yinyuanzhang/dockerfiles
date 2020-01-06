FROM alpine/git
MAINTAINER entitystream
COPY monsterDB/pom.xml /buildMonster/
COPY monsterDB/src /buildMonster/src/
WORKDIR /buildIdentiza/
RUN git clone https://github.com/entitystream/identiza
FROM maven:3.5.2-jdk-8-alpine AS MAVEN_BUILD
COPY --from=0 /buildMonster/ /build/
COPY --from=0 /buildIdentiza/identiza/identiza /buildIdentiza/
WORKDIR /buildIdentiza/
RUN mvn install -P simple-profile
WORKDIR /build/
RUN mvn install -P uber-jar-profile -Dmaven.test.skip=true
FROM openjdk:8
RUN mkdir /monsterDB
RUN mkdir /monsterDB/data
COPY --from=MAVEN_BUILD /build/target/monsterDB.jar /monsterDB
VOLUME ["/monsterDB"]
ENV nodeNum=0
ENV replicaSet=null
ENV port=27018
ENTRYPOINT java -jar /monsterDB/monsterDB.jar -s -p ${port} -db /monsterDB/data -n ${nodeNum} -rs ${replicaSet}
