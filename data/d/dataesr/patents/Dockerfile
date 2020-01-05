FROM python:3.6.5-alpine

# set working directory
WORKDIR	/srv

# add and install requirements
COPY requirements.txt /srv/requirements.txt
RUN	pip	install -r requirements.txt --proxy=${HTTP_PROXY}

# add app
COPY . /srv
