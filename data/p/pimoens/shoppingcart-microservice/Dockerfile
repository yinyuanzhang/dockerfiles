# Use an official Python runtime as an image
FROM python:3.5.2
LABEL maintainer="Pieter Moens, Pieter.Moens@UGent.be"

RUN apt-get update

# The EXPOSE instruction indicates the ports on which a container will listen for connections
EXPOSE 5012

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this
# instruction creates a directory with this name if it doesn’t exist
COPY . /shoppingcart-microservice
WORKDIR /shoppingcart-microservice

# Install any needed packages specified in requirements.txt
COPY requirements.txt /shoppingcart-microservice
RUN pip install -r requirements.txt

# Run application when the container launches
ENTRYPOINT [ "python" ]
CMD [ "shoppingcart-microservice.py" ]
