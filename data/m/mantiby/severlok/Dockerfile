# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends ssh git gcc default-libmysqlclient-dev python3-dev

# Add directories
RUN mkdir -p /srv/severlok/src/ && \
    mkdir -p /srv/severlok/static/ && \
    mkdir -p /srv/severlok/media/ && \
    mkdir -p /var/log/severlok/ && \
    mkdir -p /root/.ssh/

# Copy bitbucket deploy key
COPY deploy/deploy.key /root/.ssh/id_rsa

# Add bitbucket to known hosts
RUN chmod 400 /root/.ssh/id_rsa && \
    touch /root/.ssh/known_hosts && \
    ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts

# Clone repo
WORKDIR /srv/severlok/src/
RUN git init && \
    git remote add origin git@bitbucket.org:manti_by/severlok.git

# Install any necessary packages specified in requirements
COPY deploy/requirements/base.txt /tmp/base.txt
COPY deploy/requirements/prod.txt /tmp/prod.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/prod.txt

# Run gunicorn
EXPOSE 8228
WORKDIR /srv/severlok/src/app/
CMD exec uwsgi --wsgi-file core/wsgi.py --http 0.0.0.0:8228 \
    --master --processes 2 --threads 2 \
    --disable-logging --log-4xx --log-5xx --logto /var/log/severlok/uwsgi.log
