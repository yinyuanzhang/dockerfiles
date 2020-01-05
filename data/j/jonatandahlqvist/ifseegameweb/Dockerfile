# Dockerfile for game server
FROM python:3.7

EXPOSE 5000

# Set an environment variable with the directory
# where we'll be running the app
ENV APP /app
#ENV REDIS_LOCAL "True"

# # Use in order to work with local redis in docker-compose
# ENV REDIS_HOST 'redis'
# ENV REDIS_PWD ''

# Instruct Flask where to find resources
ENV STATIC_URL /static
ENV STATIC_PATH /app/the_see_game/static

# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir /app
WORKDIR /app/the_see_game

# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .

# Install Python dependencies
# RUN pip install  --proxy http://UserName:Password@gia.sebank.se:8080 --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# We copy the rest of the codebase into the image
COPY . /app/

CMD [ "python", "../runserver.py" ]
# docker run -it -rm -p 5000:5000 --rm --name=wss wserver:0.2 bash
# docker run -it -p 80:8081 -e PORT="8081" --rm --name=wss wserver2:0.2 bash
# docker run -d -p 80:8081 -e PORT="8081" --name=wss wserver2:0.2
# docker run -d -p 5656:5656 -e PORT="5656" --name=wss wserver2:0.2
# docker run -p 5656:5656 -e LOG_LEVEL="debug" --name=wss4 wserver2:0.2
# docker run -it -p 5656:5656 -e LOG_LEVEL="debug" --rm --name=wss wserver2:0.2 bash
# docker run -it -p 5000:5000 --rm --name=wss wserver:0.01 bash
# docker run -p 5000:5000 --rm --name=wss wserver:0.01
# docker build --file=DockerfileWebServer --tag=wserver:0.01 .
