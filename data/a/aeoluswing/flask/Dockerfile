FROM python:3.6.5-alpine

RUN pip install flask

RUN pip install Flask-SQLAlchemy

RUN mkdir -p /src

COPY src /src/

WORKDIR /src

VOLUME /src/

EXPOSE 5000

CMD ["python3","main.py"]