FROM python:3.6

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

RUN mkdir /inti
RUN mkdir /www
RUN mkdir /www/static

COPY ./inti /inti

WORKDIR /inti
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE inti.settings.staging

EXPOSE 9000
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:9000", "inti.wsgi:application"]