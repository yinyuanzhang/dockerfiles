FROM python:3.7


COPY Pipfile /Pipfile

RUN pip install pipenv \
 && pipenv install --system --skip-lock

COPY ./slibrary ./slibrary

ENV HOST='0.0.0.0'
ENV PORT='5000'

EXPOSE 5000

ENTRYPOINT [ "python", "slibrary/__main__.py" ]