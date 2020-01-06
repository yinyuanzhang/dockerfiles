FROM google/cloud-sdk:alpine
LABEL NAME="KindleEar"
LABEL version="1.26.6"

RUN gcloud components install app-engine-python app-engine-python-extras
RUN git clone https://github.com/cdhigh/KindleEar.git /app
RUN apk --update add py-lxml py-pillow py-jinja2 py-crypto

COPY cron-root /var/spool/cron/crontabs/root
COPY entrypoint.sh /entrypoint.sh

WORKDIR /app

EXPOSE 8080

ENTRYPOINT [ "/entrypoint.sh" ]