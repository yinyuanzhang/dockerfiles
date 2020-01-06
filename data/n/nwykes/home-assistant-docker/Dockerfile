FROM homeassistant/home-assistant:latest
LABEL maintainer="Nathan Wykes <nwykes@gmail.com>"

# Add Devel Repository
RUN echo "deb http://deb.debian.org/debian stretch devel" >> /etc/apt/sources.list

# Install freetds-dev
RUN apt-get update
RUN apt-get install -y freetds-dev

RUN pip3 install --no-cache-dir pymssql
