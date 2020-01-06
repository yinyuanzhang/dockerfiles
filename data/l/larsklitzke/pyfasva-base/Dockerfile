FROM larsklitzke/alpine-python3.5-mysql-scientific:latest
MAINTAINER Lars Klitzke <Lars.Klitzke@gmail.com>

RUN apk --no-cache add \
    python3-tkinter \
    cmake \
    git

RUN pip install -U\
    tqdm \
    tilemapbase \
    pymysql \
    watchdog \
    aiohttp==2.3.10 \
    SQLAlchemy \
    pymodconf

RUN apk --no-cache add linux-headers

RUN pip install -U \
    psutil

RUN apk add --upgrade sqlite
