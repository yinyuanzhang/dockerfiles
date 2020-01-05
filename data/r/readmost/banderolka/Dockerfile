FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8087

#RUN adduser --disabled-password --gecos '' myuser
CMD [ "celery", "-A","banderolka", "worker", "-l", "info"]
CMD ["python3", "manage.py", "runserver", "[::]:8087"]
