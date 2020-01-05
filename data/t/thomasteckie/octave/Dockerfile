# our base image
FROM ubuntu

# Install python and pip
RUN apt update
RUN apt-get upgrade -y
RUN apt-get install -y less nano
RUN apt-get install -y octave


# run the application
CMD ["octave"]
