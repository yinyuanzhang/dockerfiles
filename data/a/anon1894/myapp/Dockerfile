FROM openjdk:8-jre-alpine
# Create the home directory for the new app user.
RUN mkdir -p /home/app

# Set the home directory to our app user's home.
ENV HOME=/home/app
ENV APP_HOME=/home/app/demo
## SETTING UP THE APP ##
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
ADD target/*.jar $APP_HOME/app.jar
EXPOSE 8080
ENTRYPOINT exec java -jar $APP_HOME/app.jar --spring.profiles.active=docker

