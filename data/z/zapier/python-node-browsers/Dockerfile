FROM circleci/python:3.7.3-stretch-node-browsers

# System

USER root

# Python

ENV PYTHONDONTWRITEBYTECODE true

# Poetry

ENV POETRY_VERSION=1.0.0
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"

# Firefox

RUN sudo wget https://ftp.mozilla.org/pub/firefox/releases/70.0/linux-x86_64/en-US/firefox-70.0.tar.bz2 && \
sudo tar -xjf firefox-70.0.tar.bz2 && \
sudo rm -rf /opt/firefox* && \
sudo rm firefox-70.0.tar.bz2 && \
sudo mv firefox /opt/firefox70 && \
sudo ln -sf /opt/firefox70/firefox-bin /usr/bin/firefox && \
firefox --version

RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz \
| sudo tar xz -C /usr/local/bin && \
geckodriver --version

# Media

RUN sudo rm -rf /var/lib/apt/lists/* && sudo apt-get update && apt-get install imagemagick ffmpeg graphviz

# Lighthouse

RUN npm install -g lighthouse@3

# Validation

COPY verchew.ini /opt/
RUN pip install --upgrade pip verchew
CMD verchew --root=/opt/ --exit-code
