FROM ekrem6nel/devops-docker-base
MAINTAINER ekrem@xellucia.org

COPY . /app
WORKDIR /app

RUN mvn clean compile package

WORKDIR /app/target

EXPOSE 8080:8080

CMD java -jar mvp.jar