FROM schemaspy/schemaspy

USER root
RUN apk --update add curl nano \
 && curl -sS -o /drivers_inc/ojdbc8.jar https://storage.googleapis.com/mpub/java/ojdbc8.jar
USER java
