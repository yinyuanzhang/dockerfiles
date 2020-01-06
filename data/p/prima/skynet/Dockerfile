FROM prima/python:3.7.2-2

RUN pip install gunicorn && \
    python -m pip install pylint && \
    apt-get update && apt-get install flake8 -y

COPY files/entrypoint.sh /entrypoint.sh

EXPOSE 8000

CMD ["/entrypoint.sh"]
