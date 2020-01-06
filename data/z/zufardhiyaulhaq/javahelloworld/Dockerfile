FROM java:8

COPY src /home/root/javahello/src
WORKDIR /home/root/javahello

RUN mkdir bin
RUN javac -d bin src/JavaHello.java

ENTRYPOINT ["java","-cp","bin", "JavaHello"]
