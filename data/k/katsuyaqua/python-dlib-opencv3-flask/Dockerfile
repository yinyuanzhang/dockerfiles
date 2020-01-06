# FROM python:3.6-onbuild
FROM python:3.6-jessie

RUN apt update
RUN apt install -y libboost-all-dev \
                   cmake \
                   build-essential
WORKDIR /
RUN git clone https://github.com/davisking/dlib.git
WORKDIR dlib/examples
RUN mkdir build
WORKDIR build
RUN cmake ..
# RUN cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1
RUN cmake --build .
WORKDIR ../..
RUN python setup.py install
# RUN python setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA
# RUN pip install flask
# COPY . /home


# WORKDIR /usr/src/app
# ENV FLASK_APP=app.py
# ENV PORT=8888
# ENV FLASK_ENV=development

# CMD ["flask", "run", "-p", "${PORT}", "-h", "0.0.0.0"]
