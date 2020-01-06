FROM python:3.6-stretch
LABEL maintainer="Vijay Sekhri"

RUN pip3 install --no-cache requests flask pyopenssl
COPY server.py /server.py
ADD entrypoint.sh /entrypoint.sh
ENV PATH /:$PATH
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


