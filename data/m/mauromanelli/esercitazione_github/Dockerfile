FROM java:7
#COPY HelloWord.java /
WORKDIR   /home/javahelloword/
COPY src /home/javahelloword/src
#RUN javac HelloWord.java
RUN mkdir ban
RUN mkdir bin
RUN javac  -d bin src/HelloWord.java
#ENTRYPOINT ["java","HelloWord"]
ENTRYPOINT ["java","-cp","bin","HelloWord"]