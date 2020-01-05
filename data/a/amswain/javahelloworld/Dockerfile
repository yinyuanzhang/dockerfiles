FROM java:8

COPY src /root/javahelloworld/src
WORKDIR /root/javahelloworld
ENV FOO bar
ENV FOO2 bartwotwo

RUN mkdir bin
RUN javac -d bin src/HelloWorld.java

ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]

