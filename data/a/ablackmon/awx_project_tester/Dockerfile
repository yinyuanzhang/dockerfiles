FROM python:3
MAINTAINER ablackmon@andrewblackmon.com

RUN pip3 install yamllint ansible-lint black pylint

RUN pip3 install pandevice requests requests-cache pytz orionsdk pymsteams

RUN mkdir -p /home/tester/

WORKDIR /home/tester
