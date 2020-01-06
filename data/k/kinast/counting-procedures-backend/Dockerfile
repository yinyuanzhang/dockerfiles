# to build this run: docker build -t kinast/counting-procedures-backend .
#
# to run this in development mode, modify the local path and then run The port must be 8090 because it's hardcoded in the frontend for now:
# docker run -it --name backend -v E:/bitbucket/backend/counting-procedures-rest:/app/counting-procedures-rest -p 8090:8090 kinast/counting-procedures-backend:latest
#
# to run this in normal mode run either -it (interactive) or -d
# docker run -it --name backend -p 8090:8090 kinast/counting-procedures-backend:latest
# install maven and java development kit
FROM maven:3.5.4-jdk-8
RUN mkdir /app
WORKDIR /app
#RUN git clone https://kibsi:53R8hSJWUQKGDnFxL8SK@bitbucket.org/kibsi/counting-procedures-rest.git
COPY . /app
#WORKDIR /app/counting-procedures-rest
RUN mvn clean install dependency:copy-dependencies
VOLUME /app
EXPOSE 8090
#ENTRYPOINT /bin/bash
CMD mvn exec:java