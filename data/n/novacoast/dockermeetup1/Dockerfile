FROM ubuntu:12.04
 
#Install Ruby 1.9.1
RUN apt-get update
RUN apt-get upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install ruby1.9.1 ruby1.9.1-dev make

#Install nodejs
RUN apt-get install -y nodejs
 
#Install Jekyll
RUN gem install --no-rdoc --no-ri jekyll

COPY /webapp /src
 
WORKDIR /src
 
EXPOSE 80
 
CMD ["jekyll", "serve", "-P 80", "--watch"]
