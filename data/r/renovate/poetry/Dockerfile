FROM renovate/pip@sha256:b28352f8b7f9e467e36f5d9046f0a08c660bc50cce2b921e90b3b768d396230b

ENV HOME=/home/ubuntu

ENV POETRY_VERSION=1.0.0

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --version ${POETRY_VERSION}

ENV PATH="${HOME}/.poetry/bin:$PATH"
RUN ${HOME}/.poetry/bin/poetry config virtualenvs.in-project false
