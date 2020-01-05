FROM python:3-alpine

WORKDIR /usr/src/brisk

# This is a separate copy becuase it is one layer and it is rarely change
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Code change more frequently so the build will always start from here
COPY . .

CMD [ "python", "./main.py" ]

LABEL maintainer="ysinjab@gmail.com"
