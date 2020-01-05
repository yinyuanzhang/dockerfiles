FROM python:3

MAINTAINER Miguel imiguel10@correo.ugr.es

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

WORKDIR src/

EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "porradepapp:app"]

