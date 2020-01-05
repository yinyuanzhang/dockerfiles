#
# Dockerfile for sickbeard (french version)
#
FROM python:2

MAINTAINER Xavier Logerais <xavier@logerais.com>

# Create a dedicated user
RUN useradd -m sickbeard

# Download pre-requisites
RUN pip install cheetah

# Download latest version
USER sickbeard
WORKDIR /home/sickbeard
RUN git clone https://github.com/sarakha63/Sick-Beard ./app

# Create a volume for series
USER sickbeard
WORKDIR /home/sickbeard
RUN mkdir series

# Expose the sickbeard home
VOLUME /home/sickbeard

# Expose the listening port
EXPOSE 8081

# Launch it
USER sickbeard
WORKDIR /home/sickbeard
CMD [ "python", "app/SickBeard.py" ]
