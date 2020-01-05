# Builds a Docker image to run docker-example-app1.  The base image will handle
# adding any application files and required dependencies to this image.
#
FROM ubuntu:18.10
MAINTAINER Kevin Liu <kevin.liuzhong@gmail.com>

#RUN echo "deb http://ftp.uk.debian.org/debian jessie-backports main">>/etc/apt/sources.list
RUN apt-get update && apt-get install -y git python3.7 python3-pip ffmpeg fonts-wqy-zenhei fonts-noto-cjk fonts-noto-color-emoji fonts-emojione locales
ENV APP_DIR /app
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR
COPY . $APP_DIR/

RUN pip3 install -r $APP_DIR/api-requirements.txt

# Expose the port where uWSGI will run
EXPOSE 80

# If running this app behind a webserver using the uwsgi protocol (like nginx),
# then use --socket.  Otherwise run with --http to run as a full http server.
#CMD ["uwsgi", "-b", "65536", "--http", "0.0.0.0:80", "--wsgi-file", "/app/api/app.py", "--callable", "app", "--processes",  "2", "--threads", "4"]

CMD ["python3", "-u", "/app/app-api.py"]