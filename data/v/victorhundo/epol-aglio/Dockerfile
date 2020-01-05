FROM node:latest

# Create app directory
RUN mkdir -p /api
WORKDIR /api

# Install apache
RUN apt-get update && apt-get install -y \
    apache2 \
&& rm -rf /var/lib/apt/lists/*

# Install Aglio
RUN npm install -g aglio

COPY ./start-script /
EXPOSE 80
CMD ["bash", "/start-script"]
