# Use Debian
FROM debian:latest

MAINTAINER WaaaghNL <docker@waaagh.nl>

# Define environment variable
ENV APIURL https://api.scantheweb.org
ENV RATE 400
ENV OUTPUTDIR ./output/ #with tailing /

#update
RUN apt-get update

#Install any needed packages
RUN apt-get install -y apt-utils
RUN apt-get install -y git
RUN apt-get install -y build-essential
RUN apt-get install -y curl
RUN apt-get install -y wget
RUN apt-get install -y libpcap-dev
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
#RUN pip install httpclient
#RUN pip install json

# Clone masscan git repo
##RUN git clone https://github.com/robertdavidgraham/masscan /opt/masscan
##WORKDIR /opt/masscan

# Make masscan
##RUN make -j

# Copy binary
##RUN cp /opt/masscan/bin/masscan /usr/local/bin

#Worker
# Set the working directory to /app
WORKDIR /worker

# Copy the current directory contents into the container at /app
COPY . /worker

# Run app.py when the container launches
CMD ["python", "worker.py"]

# Launch Bash
#CMD ["/bin/bash"]