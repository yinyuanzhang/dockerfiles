# Using official python runtime base image
FROM python:3.7.2-stretch
# Environment Variables

ENV AMQP_HOST myaccess
ENV AMQP_PORT mysecret
ENV AMQP_USER myendpoint.de
ENV AMQP_PASS mybucket  
ENV AMQP_RECEIVE_QUEUE mysecret
ENV AMQP_SEND_QUEUE myid

RUN apt-get update && \
    apt-get install -y --no-install-recommends libatlas-dev 
# libatlas3gf-base
RUN apt-get install -y libxml2-dev python-numpy libicu-dev

# Set the application directory
WORKDIR /app

# Install our requirements.txt
RUN pip install --upgrade pip
RUN pip install cython
RUN pip install numpy && \
    pip install --upgrade cython && \
    pip install lxml && \
	pip install pika
#	pip install nltk && \
RUN pip install dragnet flask


#ADD requirements.txt /app/requirements.txt
#RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /app




# Define our command to be run when launching the container
CMD ["python", "app.py"]
