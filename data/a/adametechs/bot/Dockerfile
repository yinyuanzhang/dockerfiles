FROM adametechs/maven:latest

ADD . /app/
WORKDIR /app
RUN mvn install
RUN ["chmod", "+x", "/usr/local/bin/mvn-entrypoint.sh"]

CMD ["./mvnw"]

