FROM python:3.6.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
COPY /django_discovery /app/
COPY manage.py /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN chown -R $USER:$USER .
#RUN django-admin.py startproject djangoproject
#RUN mkdir /app/djangoproject/media && mkdir /app/djangoproject/static
#VOLUME /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# RUN chmod +x docker-entrypoint.sh
# ENTRYPOINT ["docker-entrypoint.sh"]
