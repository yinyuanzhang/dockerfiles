FROM java:7
MAINTAINER Docker Training <main@domain.xyz>

ENV FOO bar



COPY src /home/root/javahelloworld/src

WORKDIR /home/root/javahelloworld
RUN mkdir bin && \
    javac -d bin src/HelloWorld.java

ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]
