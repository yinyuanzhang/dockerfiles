FROM java:8

COPY src /home/docker/javahelloworld/src
WORKDIR /home/docker/javahelloworld
ENV FOO bar2
RUN mkdir bin
RUN javac -d bin src/HelloWorld.java
ENTRYPOINT ["java","-cp","bin", "HelloWorld"]



