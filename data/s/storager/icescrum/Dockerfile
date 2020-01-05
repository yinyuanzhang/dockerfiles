FROM openjdk:8-jre-alpine
EXPOSE 8080
ENV APP_DIR=/opt/icescrum
USER root
RUN adduser icescrum -s /bin/sh -h /opt/icescrum -D
ADD --chown=icescrum:icescrum start.sh /
USER icescrum
CMD [ "/bin/sh", "/start.sh" ]