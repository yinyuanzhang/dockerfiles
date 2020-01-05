#################################################################
# Dockerfile for building a Hybris image with initialized content
# Prerequisites: running MySQL container
# the MySQL container is initialized and saved as well
# for Docker version: v1.3+
#################################################################

FROM anapsix/alpine-java:8_server-jre


# Set working directory
ENV APP_HOME /requalize
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# copy app jar
ADD requalize-web.jar $APP_HOME/

# copy entrypoint
ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["java -jar -Dspring.profiles.active=prod requalize-web.jar"]
