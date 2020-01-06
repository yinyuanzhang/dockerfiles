FROM python:3

RUN dpkg --add-architecture i386 && apt-get update && apt-get install -qq -y libc6:i386 libncurses5:i386 libstdc++6:i386 multiarch-support

WORKDIR /usr/src/app
COPY . .
VOLUME ["/data"]

ENTRYPOINT ["python","./dezoomify.py"]
