FROM ubuntu:14.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    python-pip
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN mkdir /proyecto
RUN cd /proyecto
RUN git clone https://github.com/pablinho6699/corcubion-pagina
WORKDIR /code/corcubion-pagina/corcu
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
