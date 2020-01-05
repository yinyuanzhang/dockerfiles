FROM python:3.4-alpine
MAINTAINER Madan Thangavelu (madankumar.t@gmail.com)
LABEL version="1.0"
LABEL description="Assistant to help local docker installations"
RUN apk add --no-cache bash
RUN apk add --no-cache curl
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
CMD ["python", "app.py"]
