FROM python:3.7-alpine

RUN pip3 install \
  flake8 \
  flake8-builtins \
  flake8-commas \
  flake8-comprehensions \
  flake8-docstrings \
  flake8-quotes \
  bandit

WORKDIR /src

COPY check.sh /usr/local/bin
COPY check_docs.sh /usr/local/bin
COPY check_sec.sh /usr/local/bin

CMD ["check.sh"]
