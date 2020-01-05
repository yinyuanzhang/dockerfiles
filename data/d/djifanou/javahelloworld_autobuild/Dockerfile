FROM java:8
MAINTAINER Djifanou Kpetemey <djifanou.kpetemey@orange.com>
COPY src /home/root/javahelloworld/src
WORKDIR /home/root/javahelloworld
RUN mkdir bin
RUN javac -d bin src/HelloWorld.java
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]
ENV FOO bar
