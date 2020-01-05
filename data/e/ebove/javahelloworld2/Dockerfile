# third version
FROM java:7
RUN apt-get -y install curl
COPY HelloWorld.java /
RUN javac HelloWorld.java
ENTRYPOINT [ "java", "HelloWorld" ]
