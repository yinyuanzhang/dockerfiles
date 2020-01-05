from java:7
COPY src /home/root/javahelloworld/src
WORKDIR /home/root/javahelloworld
RUN apt-get update && apt-get install -y node
RUN mkdir bin
RUN javac -d bin src/HelloWorld.java
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]
