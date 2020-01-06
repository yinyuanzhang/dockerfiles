FROM ubuntu:16.04
LABEL maintainer='david@reflashed.com'

# Install python and pip
RUN apt-get update --yes
RUN apt-get install --yes python3 python3-pip python-dev sqlite3

# Install uwsgi dependencies
#   - https://stackoverflow.com/questions/21669354/rebuild-uwsgi-with-pcre-support
#   - https://stackoverflow.com/questions/27308288/uwsgi-unrecognized-option-https
RUN apt-get install --yes libpcre3 libpcre3-dev libssl-dev

# Install nginx
RUN apt-get install --yes nginx

# Install screen and rabbitmq
RUN apt-get install --yes screen rabbitmq-server

# Install flask and uwsgi with pip3
ADD ./requirements.txt /etc/python3/requirements.txt
RUN pip3 install -r /etc/python3/requirements.txt

# Add everything in the git repo to the container
ADD --chown=www-data:www-data . /foc-web

# Install node 12.x and npm
RUN apt-get update --yes
RUN apt-get install --yes curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
RUN apt-get install --yes nodejs

# Install npm packages
WORKDIR /foc-web/flask
RUN npm install

# Run webpack
RUN npm run prod

# Set up flask environmental variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=app.py
ENV ENVIRON=PROD

# Scripts that start uWSGI and nginx
#   You must be in the dir that contains "app.py" for our uwsgi config to work
CMD /foc-web/server/start.sh
