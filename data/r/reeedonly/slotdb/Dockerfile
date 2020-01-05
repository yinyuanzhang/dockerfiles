FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD ./src /src

EXPOSE 8000

# RUN python3 src/manage.py migrate
# CMD python3 src/manage.py runserver 0.0.0.0:8000
