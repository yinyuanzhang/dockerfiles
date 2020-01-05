FROM python:3.7
RUN pip install psycopg2
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
ENTRYPOINT ["/bin/sh", "docker-entrypoint.sh"]