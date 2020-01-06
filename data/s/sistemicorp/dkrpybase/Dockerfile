# dkrpybase image
# this image builds the targets, so it has everything...
FROM python:3.6-slim

RUN apt-get update && apt-get install -y --no-install-recommends gcc g++

ADD requirements.txt /

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

VOLUME ["/tmp"]
WORKDIR /tmp

# python3
ENTRYPOINT ["python"]

# Build Image:
# docker build --no-cache --pull -t dkrpybase .
#
# To build python source:
# docker run -ti -v $(pwd):/tmp dkrpybase build_compile.py --main lente --flask --lang 3 --compile --rm-source --name lente
# docker run -ti -v $(pwd):/tmp dkrpybase build_compile.py --main prism --flask --lang 3 --compile --rm-source --name prism

# Debugging
# To get a shell into this container:  docker run -it --entrypoint "/bin/sh" sistemicorp/dkrpybase:latest
#
# To search for files: find / -name Python.h
