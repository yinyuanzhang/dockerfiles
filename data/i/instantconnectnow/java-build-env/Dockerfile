FROM maven:3.5.4-jdk-8

RUN apt-get update
RUN apt-get install rpm -y
RUN apt-get install xorriso -y
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN apt-get clean

# Some IPICS shell scripts expect cut to be under /bin
RUN ln -s /usr/bin/cut /bin/cut 

