FROM python:2.7

RUN apt-get update \
		&& apt-get install -y tcsh lib32z1 \
		&& rm -rf /var/lib/apt/lists/

RUN easy_install hashlib
RUN pip install sqlalchemy Flask-API mysql-python


WORKDIR /app

RUN  cd /home && curl http://www.compbio.dundee.ac.uk/jpred3/legacy/jnet/download/jnet.linux.tar.gz |  tar xz

WORKDIR /app/
COPY models /app/models
COPY *.py /app/
# LIbrary file, from ../
COPY library.py /app/
RUN chmod +x *.py

COPY runSingleJnet.sh /home/jnet/jnet.sh
COPY run.py /app/
COPY library.py /app/


RUN chmod +x /home/jnet/jnet.sh
RUN chmod +x /app/*.py
RUN mkdir /home/jnet/output
RUN echo "latest" >> /home/jnet/VERSION
EXPOSE 5000 80
ENV FLASK_APP=run.py
ENTRYPOINT [ "flask", "run" , "--host=0.0.0.0"]
