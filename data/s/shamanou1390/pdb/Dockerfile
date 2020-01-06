FROM python:2.7.14

RUN apt-get update \
		&& apt-get install -y \
		    tcsh \
		    build-essential  python-biopython\
		    gcc-multilib \
		&& rm -rf /var/lib/apt/lists/

RUN easy_install hashlib
RUN pip install  sqlalchemy numpy scipy biopython Flask-API mysql-python

WORKDIR /app/
COPY models /app/models
COPY *.py /app/
# LIbrary file, from ../
COPY library.py /app/
RUN curl -L https://files.pythonhosted.org/packages/c7/fa/8e68cdcbdc083acc1c57e369277687a4ada2ff6df421699977cedfa255a2/ProDy-1.9.3.tar.gz | tar xz

RUN cd ProDy-1.9.3 && python setup.py install
RUN chmod +x *.py
RUN mkdir /app/output
COPY pdb.py /app/
COPY library.py /app/
COPY run.py /app/

RUN chmod +x /app/*
EXPOSE 5000 80
RUN echo "latest" >> /app/VERSION

ENV FLASK_APP=run.py
ENTRYPOINT [ "flask", "run" , "--host=0.0.0.0"]
