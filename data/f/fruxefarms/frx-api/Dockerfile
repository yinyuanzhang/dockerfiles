# FRUXE API Dockerfile.
FROM python:3.7
COPY ./app /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]