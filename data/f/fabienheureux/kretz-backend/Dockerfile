FROM python:3
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
# RUN apt-get update && apt-get install -y curl autoconf automake libtool pkg-config
# RUN git clone https://github.com/openvenues/libpostal 
# COPY ./scripts/*.sh /libpostal/
# WORKDIR /libpostal
# RUN ./build_libpostal.sh
ENV ENVIRONMENT dev
ENV APP web 
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["sh", "-c", "make start-$APP-$ENVIRONMENT"]
