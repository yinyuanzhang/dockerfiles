FROM java:8
COPY src/HelloWorld.java /home/root/javahelloworld/src/
WORKDIR /home/root/javahelloworld
RUN mkdir -pv /home/root/javahelloworld/bin
RUN javac -d bin src/HelloWorld.java
RUN apt-get  install -y wget
ENTRYPOINT ["java","-cp","bin","HelloWorld"]
