FROM python:2.7

RUN apt-get update \
		&& apt-get install -y tcsh\
		&& rm -rf /var/lib/apt/lists/

RUN easy_install hashlib
RUN pip install sqlalchemy Flask-API mysql-python

WORKDIR /app/

RUN cd /home/ && curl http://bioinfadmin.cs.ucl.ac.uk/downloads/psipred/psipred.4.02.tar.gz | tar xz
COPY models /app/models
COPY *.py /app/
# LIbrary file, from ../
COPY library.py /app/
RUN chmod +x *.py

COPY run.py /app/
COPY library.py /app/
#RUN echo -ne "4.01" >> /home/VERSION
RUN echo "latest" > /home/psipred/VERSION
RUN chmod +x /app/*.py
EXPOSE 5000 80
ENV FLASK_APP=run.py
ENTRYPOINT [ "flask", "run" , "--host=0.0.0.0"]
