FROM java:7

COPY src /home/root/javahelloworld/srv
WORKDIR /home/root/javahelloworld
RUN mkdir bin
RUN javac -d bin srv/HelloWorld.java
RUN apt-get update && apt-get install -y vim

ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]
