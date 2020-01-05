FROM python:3.7-alpine

# Set the working directory
WORKDIR /app

# Set the execution command
CMD [ "python", "/app/main.py" ]

# Add the source code to the image
COPY ./src /app

# Install required python packages
RUN set -ex \
  && python -m pip install --no-cache-dir --upgrade pip \
  && python -m pip install --no-cache-dir -r /app/requirements.txt
