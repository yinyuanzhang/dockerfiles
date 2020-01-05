FROM ubuntu
RUN apt update; apt install -y ruby ruby-dev rake gcc g++ make python python-dev wget
RUN cd; wget https://bootstrap.pypa.io/get-pip.py; python get-pip.py; pip install jupyter
RUN apt install -y libzmq3-dev libtool-bin autoconf; gem install rbczmq iruby pry

EXPOSE 8888
CMD iruby notebook --no-browser --ip='*' --port 8888

