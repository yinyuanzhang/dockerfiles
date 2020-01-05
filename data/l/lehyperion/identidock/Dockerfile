FROM python:3.6

RUN apt-get update && apt-get install -y dos2unix
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask==0.10.1 uWSGI==2.0.8 requests==2.5.1 redis==2.10.3
WORKDIR /app
COPY app /app
COPY cmd.sh /
RUN dos2unix /cmd.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*
EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]