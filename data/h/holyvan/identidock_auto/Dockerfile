FROM python

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask uWSGI
WORKDIR /app
COPY app /app
COPY cmd.sh /

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]
# CMD ["python","identidock.py"]
# CMD ["uwsgi","--http","0.0.0.0:9090","--wsgi-file","/app/identidock.py","--callable","app","--stats","0.0.0.0:9191"]
