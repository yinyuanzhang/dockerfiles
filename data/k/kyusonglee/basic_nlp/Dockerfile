FROM python:3.6.7
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt && \
    curl -O "https://convmind-models.s3.us-east-2.amazonaws.com/basic-models/model.tar" && \
    tar -xvf model.tar
COPY . .
EXPOSE 6000
CMD [ "gunicorn", "-b", "0.0.0.0:6000", "-w", "4", "wsgi:application"]