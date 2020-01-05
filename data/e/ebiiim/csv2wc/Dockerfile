FROM python:3.7

EXPOSE 8080 8081

WORKDIR /app
COPY . /app

RUN useradd uwsgi
RUN chown uwsgi tmp
RUN sed -i -e "/logto/d" app.ini

RUN pip3 install -r requirements.txt
RUN python3 setup.py

USER uwsgi
CMD ["uwsgi", "--ini", "app.ini"]

