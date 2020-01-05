FROM python:alpine

LABEL maintainer="Zachary Wilson <wilsonze@gmail.com>"

WORKDIR /usr/src/app
RUN pip install --no-cache-dir pipenv

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP worklog:factory
ENV FLASK_ENV production

EXPOSE 5000

ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock
ONBUILD RUN pipenv install --deploy --system

ENTRYPOINT ["python", "-m", "flask"]
CMD ["run", "--host", "0.0.0.0"]
