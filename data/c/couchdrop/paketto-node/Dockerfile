FROM ubuntu:latest
RUN apt-get update -y && apt-get install -y supervisor software-properties-common vim
RUN apt-get install -y  openjdk-8-jdk maven supervisor python-pip python-dev build-essential postgresql-client-common libpq-dev curl libssl-dev libcurl4-openssl-dev

WORKDIR /app
COPY . /app

COPY env/supervisor.conf /etc/supervisor/conf.d/

# Install the UWSGI applications
RUN pip install -r requirements.txt

CMD ["supervisord", "-n"]