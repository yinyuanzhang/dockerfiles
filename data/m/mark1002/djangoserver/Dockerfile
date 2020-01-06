FROM python:3
MAINTAINER mark chang <ak0922747401@gmail.com>

WORKDIR /djangoserver

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8002
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8002"]