FROM balenalib/aarch64-alpine-python
RUN [ "cross-build-start" ]

RUN apk add ffmpeg python3-dev git gcc musl-dev linux-headers

ADD ./requirements.txt .

RUN python3 -m pip install -r requirements.txt

ADD . /

CMD "python3" "/api/main.py"

RUN [ "cross-build-end" ]

