FROM python:alpine

RUN apk add git py3-dateutil && pip3 install apscheduler django django-crispy-forms youtube-dl google-api-python-client google_auth_oauthlib oauth2client python-dateutil

 RUN echo "**** install app ****" && \
 git clone --depth 1  https://github.com/chibicitiberiu/ytsm.git /app && cd /app

RUN mkdir -p /config && sed -i "s/os.path.join\(BASE_DIR, 'db.sqlite3'\)/\/config\/db.sqlite3/" /app/YtManager/settings.py && sed -i "s/MEDIA_ROOT = 'data\/media'/MEDIA_ROOT = '\/config\/media'/" /app/YtManager/settings.py
RUN mv /app/config/* /config/ && rm -rf /app/config
RUN ln -s /config /app/config
RUN cd /app && python3 manage.py migrate

# add local files
COPY root/ /

# ports and volumes
EXPOSE 4040
WORKDIR /app
VOLUME /config