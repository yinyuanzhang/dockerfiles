# note that order matters in terms of docker build layers. Least changed near start to most changed...
# This image will be based on the official nodejs docker image
FROM python:3.8.0-buster

RUN apt-get update && \ 
  apt-get install -yqq apt-transport-https 
RUN echo "deb https://deb.nodesource.com/node_10.x jessie main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
  wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs yarn && \
  rm -rf /var/lib/apt/lists/*


VOLUME ["/srv/app/ssl"]
EXPOSE 80
ENV PORT 80
# Because python3 is not valid in this container. Boo.
ENV PYTHON_EXECUTABLE python 

# Commands will run in this directory
WORKDIR /srv/app

# Add build file
COPY ./package.json package.json

# Handle NPM Token Management
ARG NPM_TOKEN
COPY .npmrc-deploy .npmrc

# Install dependencies and generate production dist
RUN npm install
RUN rm -f .npmrc

# Copy the code for the prod container.
# This seems to not cause any problems in dev when we mount a volume at this point.
COPY ./app app
COPY ./config config
COPY ./wolfram-scripts wolfram-scripts

# Python setup.
COPY requirements.txt requirements.txt
# RUN pip --version
RUN pip install --no-cache-dir -r requirements.txt

CMD ["npm", "start"]
