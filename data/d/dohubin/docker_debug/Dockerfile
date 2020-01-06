FROM node:buster

RUN apt-get update && apt-get install -y python-pip python libgtk-3-0 
RUN apt-get update && apt-get install -y --no-install-recommends apt-transport-https libxt6 xvfb libnss3 libxss1 libgconf-2-4 libasound2 nodejs npm htop && rm -rf /var/lib/apt/lists/*
RUN pip install --user Jinja2 cryptography fonttools brotli
