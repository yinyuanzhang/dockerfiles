FROM mongo:3.4

ENV MONGO_HOST="127.0.0.1:27017" \
    BUCKET_URI="" \
    GOOGLE_APPLICATION_CREDENTIALS=""

COPY prepareEnv.sh /opt/prepareEnv.sh

RUN bash -x /opt/prepareEnv.sh

COPY bkp.sh /opt/bkp.sh

ENTRYPOINT ["/bin/bash","/opt/bkp.sh"]
CMD [ "dump" ]
