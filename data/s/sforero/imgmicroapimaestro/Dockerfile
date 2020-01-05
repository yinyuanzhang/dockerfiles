FROM sforero/imagenbasems

ENV USER root

VOLUME /tmp

COPY . .

RUN mvn clean install

RUN chmod a+x ./entrypoint.sh
RUN chown $USER:$USER ./entrypoint.sh
RUN chown $USER:$USER ./kms_utils.sh; exit 0

ENTRYPOINT ["./entrypoint.sh"]