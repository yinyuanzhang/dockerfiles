FROM ubuntu:16.04

RUN apt-get update -q
#COPY /tmp .
#ENV LOG_FILE /tmp/prova.txt
#RUN mkdir /cartellaprova
#RUN echo "prova" > /tmp/prova.txt
RUN apt-get install time -y
CMD ["time", "dd", "bs=1M", "count=1024", "if=/dev/zero", "of=/simple-container-benchmarks-writetest", "conv=fdatasync"]
