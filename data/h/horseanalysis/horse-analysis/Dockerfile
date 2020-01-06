FROM python:3.7.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080
CMD [ "./wait-for-it.sh", "db:3306", "--", "python", "manage.py", "runserver", "0.0.0.0:8080"]
