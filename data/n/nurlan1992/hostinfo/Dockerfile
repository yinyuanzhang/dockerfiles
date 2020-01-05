# The Dockerfile defines the image's environment
# Import Python runtime and set up working directory
FROM python:3.7-alpine
WORKDIR /app
ADD . /app

# Install any necessary dependencies

RUN apk update && apk add gcc linux-headers musl-dev \ 
&& rm -rf /var/cache/apk/* \
&& pip3 install hostinfo

# Open port 80 for serving the webpage
EXPOSE 80

# Run app.py when the container launches
CMD ["python3", "hostinfoserver.py", "-p", "80"]