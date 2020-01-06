FROM python:3.7-stretch as mono

LABEL maintainer="Artem Zhukov <zhukovgreen@icloud.com>"
LABEL description="pythonnet support on Mono. Add poetry"

ENV LANG=C.UTF-8
ENV PYTHONNET_VERSION=2.4.0
ENV POETRY_VERSION=0.12.17
ENV PATH="/root/.poetry/bin:${PATH}"
ENV PIP_VERSION=19.2.3
ENV SETUPTOOLS_VERSION=41.2.0
ENV MONO_VERSION=5.4.1.6

RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
  && echo "deb http://download.mono-project.com/repo/debian stretch/snapshots/$MONO_VERSION/. main" > /etc/apt/sources.list.d/mono-official.list \
  && apt-get update \
  && apt-get upgrade -y \
  && apt install -y curl git locales locales-all make nano openssh-client \
  && apt-get install -y clang \
  && apt-get install -y mono-complete="$MONO_VERSION"\* \
  && rm -rf /var/lib/apt/lists/* /tmp/* \
  && apt autoremove -y
RUN pip install --upgrade pip=="$PIP_VERSION" setuptools=="$SETUPTOOLS_VERSION"

FROM mono as pythonnet
RUN \
  pip install pycparser \
  && pip install pythonnet=="$PYTHONNET_VERSION"

FROM pythonnet as poetry
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN poetry config settings.virtualenvs.create false

FROM poetry AS base
COPY . .
CMD ["python"]
