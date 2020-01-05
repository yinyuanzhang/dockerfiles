FROM ubuntu:bionic

ENV FLASK_PROXY_PORT 8080

# Install & upgrade packages.
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y firefox python3-pip curl

# SETUP Selenium.
RUN pip3 install -U selenium flask WSGIServer rasa-core
RUN curl -OL https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz && tar zxf geckodriver-v0.24.0-linux64.tar.gz && mv geckodriver /usr/local/bin/

# Install my application.
ADD exec.py /action/exec.py
RUN chmod +x /action/exec.py
ADD actionproxy.py /actionproxy.py

ENTRYPOINT ["python3","actionproxy.py"]
