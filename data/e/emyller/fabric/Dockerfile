FROM python:3.6
WORKDIR /app

# Install Fabric
RUN pip install fabric==2.1.3

# Set up some basic [but overridable] configuration
COPY fabric.yml /etc/fabric.yml

# Set up a custom entrypoint
ENTRYPOINT ["fab"]
