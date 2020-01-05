FROM tensorflow/tensorflow:latest-py3

WORKDIR /home/work

ADD . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN cd ./keras-contrib && python setup.py install

CMD python tensorboard/tensorboard.py
