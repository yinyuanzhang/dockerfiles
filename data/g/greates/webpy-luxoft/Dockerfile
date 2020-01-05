FROM python:3.6
RUN pip install web.py==0.40.dev0 
RUN mkdir -p /site
WORKDIR /site
ADD test /site/test
RUN mkdir -p /data
VOLUME ./data
CMD bash -c "cd /site/test; python3 app.py 8080 argument; python3 counter.py"
EXPOSE 8080

