FROM nouchka/data
MAINTAINER Jean-Avit Promis "docker@katagena.com"
LABEL version="elephantsql"

COPY start.sh /fetch.sh
RUN chmod +x /fetch.sh

ENV DB_USER     user
ENV DB_NAME     name
ENV DB_APIKEY   xxxx-yyyy-xxxx-yyyy-xxxx

CMD /fetch.sh
