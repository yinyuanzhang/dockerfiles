FROM alpine:latest


RUN apk --update --no-cache add python3 libpq \
  && apk --update --no-cache add --virtual build-dependencies postgresql-dev gcc python3-dev musl-dev \
  && pip3 install psycopg2 geopy \
  && apk del build-dependencies \
  && mkdir -p /tk102
  
ADD tk102-server-milekz /tk102
ADD POSHandler.py /tk102
ADD start.sh /

WORKDIR /tk102

#ENTRYPOINT ["/bin/sh", "-c", "python3 tk102-server-milekz"]
#CMD [ "python3", "./tk102-server-milekz" ]

CMD [ "/start.sh" ] 

EXPOSE 14600

