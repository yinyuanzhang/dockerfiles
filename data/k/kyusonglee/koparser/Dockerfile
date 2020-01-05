FROM pytorch/pytorch:latest

#RUN git clone https://github.com/kyusonglee/KoParser.git
WORKDIR /workspace/khaiii
COPY ./requirements.txt /workspace/khaiii

RUN pip install cython
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

RUN mkdir build
WORKDIR /workspace/khaiii/build

RUN cmake ..
RUN make all
RUN make resource
RUN make install
RUN make package_python
WORKDIR /workspace/khaiii/build/package_python
RUN pip install .


RUN apt-get update -y
RUN apt-get install -y language-pack-ko
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
EXPOSE 9001
WORKDIR /workspace/khaiii
CMD [ "gunicorn", "-b", "0.0.0.0:9001", "-w", "4", "wsgi:application"]
