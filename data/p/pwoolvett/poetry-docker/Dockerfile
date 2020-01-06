ARG PYTHON_TAG=3.6
FROM python:${PYTHON_TAG} as base

ARG POETRY_VERSION=1.0.0a5

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py -o get-poetry.py
RUN python get-poetry.py --preview --version ${POETRY_VERSION}
RUN rm get-poetry.py
RUN mkdir -p /root/.config/pypoetry/
RUN touch /root/.config/pypoetry/config.toml
ENV PATH="/root/.poetry/bin:$PATH"
RUN poetry config settings.virtualenvs.create false
