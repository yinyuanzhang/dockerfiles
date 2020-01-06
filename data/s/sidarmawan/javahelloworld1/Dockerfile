FROM java:8

COPY src /javahelloworld/src

WORKDIR /javahelloworld

RUN mkdir bin
RUN javac -d bin src/HelloWorld.java

ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]
