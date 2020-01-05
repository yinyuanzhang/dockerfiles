From python:3

WORKDIR /www/wwwroot/CuteOne
COPY ./ /www/wwwroot/CuteOne/
RUN pip3 install -r requirements.txt  && \
    ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi
ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]
