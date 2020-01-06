FROM python:3.6

RUN pip install invoke==1.0.0

# Easier to mount things as /app
WORKDIR /app
ENTRYPOINT inv
