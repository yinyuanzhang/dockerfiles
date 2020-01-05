FROM python:3.6

ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# RUN pip install poetry --user --pre --no-warn-script-location
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY poetry.lock .

COPY pyproject.toml .

RUN /root/.poetry/bin/poetry config settings.virtualenvs.create false && /root/.poetry/bin/poetry install --no-dev

WORKDIR /app

COPY ./score_system .

CMD ["gunicorn", "score_system.wsgi:application", "--certfile","/ssl/registry.crt", "--keyfile","/ssl/registry.key","--ssl-version","3","-k", "gevent", "-w", "4", "-b", "0.0.0.0:5000", "--log-file", "-", "--access-logfile", "-", "--capture-output"]
