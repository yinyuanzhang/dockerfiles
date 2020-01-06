FROM ubuntu:14.04
RUN apt-get update

FROM java:7
COPY JavaHelloWorld.java .

RUN javac JavaHelloWorld.java

CMD [ "java" , "JavaHelloWorld" ]
