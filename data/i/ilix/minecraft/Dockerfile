FROM openjdk

WORKDIR /mc
ADD ./run.sh /run.sh

EXPOSE 25565

ENV JAR=https://launcher.mojang.com/mc/game/1.13/server/d0caafb8438ebd206f99930cfaecfa6c9a13dca0/server.jar
CMD sh /run.sh $JAR
