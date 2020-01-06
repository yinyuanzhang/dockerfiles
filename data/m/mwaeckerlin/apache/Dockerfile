FROM mwaeckerlin/ubuntu-base
MAINTAINER mwaeckerlin

ENV DATADIR="/data"

RUN apt-get update && apt-get install -y apache2
ADD start.apache.sh /start.apache.sh

EXPOSE 80
EXPOSE 443

CMD ["/start.apache.sh"]
