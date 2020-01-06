FROM hseeberger/scala-sbt:8u171_2.12.6_1.1.5
MAINTAINER dyoshikawa

RUN sbt new playframework/play-scala-seed.g8 --name=myproject
WORKDIR /root/myproject

CMD sbt run
