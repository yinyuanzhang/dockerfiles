FROM python:latest as base

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install --editable '.'

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app
ENV FLASK_ENV production
ENV FLASK_DEBUG False

EXPOSE 5000

ENTRYPOINT ["python", "-m", "flask"]
CMD ["run", "--host", "0.0.0.0"]