FROM python:3.6

RUN pip install poetry

# download test reporter as a static binary
RUN curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 \
    >/bin/cc-test-reporter \
    && chmod +x /bin/cc-test-reporter
