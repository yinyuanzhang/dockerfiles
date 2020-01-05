FROM python:2.7.15
WORKDIR /app
COPY ./requirements.txt /app
RUN mkdir /app/model
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 4455
CMD [ "gunicorn", "-b", "0.0.0.0:4455", "-w", "4", "wsgi:application"]
