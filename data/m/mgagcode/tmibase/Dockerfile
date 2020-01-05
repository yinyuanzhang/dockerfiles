# tmibase image
# this image builds the targets, so it has everything...
FROM python:3.6-alpine

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc g++ musl-dev postgresql-dev zlib-dev linux-headers

RUN \
 apk add --no-cache --virtual jpeg-dev openjpeg-dev

# for some reason this didn't install when listed with above
RUN \
 apk add --no-cache --virtual python3-dev

ADD requirements.txt /

RUN pip3 install --no-cache-dir dominate
RUN pip3 install --no-cache-dir flask
RUN pip3 install --no-cache-dir cerberus
RUN pip3 install --no-cache-dir psycopg2-binary
RUN pip3 install --no-cache-dir sqlalchemy
RUN pip3 install --no-cache-dir py-bcrypt
RUN pip3 install --no-cache-dir Cython
RUN pip3 install --no-cache-dir pytz
RUN pip3 install --no-cache-dir bokeh==1.0.4
RUN pip3 install --no-cache-dir wget
RUN pip3 install --no-cache-dir qrcode
RUN pip3 install --no-cache-dir fpdf
RUN pip3 install --no-cache-dir requests
RUN pip3 install --no-cache-dir pyserial
RUN pip3 install --no-cache-dir pypubsub
RUN pip3 install --no-cache-dir pyvisa-py
RUN pip3 install --no-cache-dir pyusb
RUN pip3 install --no-cache-dir simple-crypt
RUN pip3 install --no-cache-dir Flask-Babel
RUN pip3 install --no-cache-dir filehash
RUN pip3 install --no-cache-dir deepdiff
RUN pip3 install --no-cache-dir ago
RUN pip3 install --no-cache-dir gitpython
RUN pip3 install -r requirements.txt --no-cache-dir

VOLUME ["/tmp"]
WORKDIR /tmp
ENTRYPOINT ["python"]

# Build Image:
# docker build -t tmibase .
#
# To build python source:
# docker run -ti -v $(pwd):/tmp tmibase build_compile.py --main TMIServer --flask --lang 3 --compile --rm-source --name TMIServer
# docker run -ti -v $(pwd):/tmp tmibase build_compile.py --main TMIStation --flask --lang 3 --compile --rm-source --name TMIStation
