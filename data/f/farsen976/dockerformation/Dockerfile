FROM java:8
WORKDIR /home/root/javahelloworld/src
COPY Hello.java ./
RUN mkdir bin && javac -d bin Hello.java
ENTRYPOINT ["java", "-cp","bin","Hello"] 
