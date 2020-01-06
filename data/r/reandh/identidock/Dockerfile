FROM python:3.7

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask uWSGI requests redis

ADD /app/ /app/
COPY /cmd.sh  /
WORKDIR /app/

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]
