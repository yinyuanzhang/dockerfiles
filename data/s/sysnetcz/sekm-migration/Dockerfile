FROM openjdk:8
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN ls
# RUN java
# RUN javac Main.java

CMD ["java", "-jar", "/target/migration-with-dependencies.jar -c 1"]
CMD ["tail", "-f", "/dev/null"]
