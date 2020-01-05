FROM alpine:3.8

WORKDIR /

COPY . .
RUN apk add --no-cache python3
RUN apk add --no-cache python3-dev
RUN apk add --no-cache py3-pip
RUN apk add --no-cache git
RUN apk add --no-cache make
RUN apk add --no-cache g++
RUN git clone https://github.com/SCADACS/snap7.git



RUN pip3 install -r source/requirements.txt

RUN cd /snap7/build/unix/ && make -f x86_64_linux.mk

RUN cp /snap7/build/bin/x86_64-linux/libsnap7.so /usr/lib/libsnap7.so
RUN cp /snap7/build/bin/x86_64-linux/libsnap7.so /usr/local/lib/libsnap7.so



#RUN apk add --update --no-cache make g++;cd /lib/snap7/build/unix;make -f x86_64_linux.mk;cp /lib/snap7/build/bin/x86_64-linux/libsnap7.so /usr/local/lib/libsnap7.so;cp /lib/snap7/build/bin/x86_64-linux/libsnap7.so /usr/lib/libsnap7.so
#RUN add-apt-repository ppa:gijzelaar/snap7
#RUN apt-get update
#RUN apt-get install libsnap71 libsnap7-dev
#RUN cp /lib/libsnap7.so /usr/local/lib/libsnap7.so;cp /lib/libsnap7.so /usr/lib/libsnap7.so

#RUN sed -r -i 's/lib_location=None/lib_location=\"\/usr\/local\/lib\/snap7.so\"/' /usr/local/lib/python3.6/dist-packages/snap7/common.py

CMD [ "python3", "/source/fogscript.py" ]