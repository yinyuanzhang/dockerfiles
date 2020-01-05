FROM alpine

# install python
RUN apk add --update py3-pip

# copy the app file
COPY app.py /usr/src/app/

# tell docker what to run by default
CMD python3 /usr/src/app/app.py
