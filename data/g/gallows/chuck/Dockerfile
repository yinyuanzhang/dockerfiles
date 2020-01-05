FROM python:alpine
LABEL maintainer="containers@computacenter.com"
RUN pip install flask gunicorn yieldfrom.urllib.request requests
COPY app/ /app/
EXPOSE 5000
WORKDIR /app/
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "wsgi:application"]