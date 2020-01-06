FROM python:3.6
RUN mkdir /app
ADD . /app
RUN pip install -r /app/app/requirements.txt
CMD ["python", "/app/app/app.py", "--port", "8080", "--monitor", "8081"]
EXPOSE 8080 8081
