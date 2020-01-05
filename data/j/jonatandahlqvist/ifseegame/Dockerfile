# Dockerfile for game server
FROM python:3.7

# Set an environment variable with the directory
# where we'll be running the app
ENV APP /app
#ENV REDIS_LOCAL "True"

# # Use in order to work with local redis in docker-compose
# ENV REDIS_HOST 'redis'
# ENV REDIS_PWD ''

# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir $APP
WORKDIR $APP

# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .

# Install Python dependencies
# RUN pip install  --proxy http://UserName:Password@gia.sebank.se:8080 --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# We copy the rest of the codebase into the image
COPY . .

CMD [ "python", "./the_see_game/the_see_game_server/" ]
# docker build --file=DockerfileGameServer --tag=gserver:0.1 .
# docker run --rm --name gss gserver:0.1
# docker run --name redis1 -d -p 6379:6379 --rm redis
