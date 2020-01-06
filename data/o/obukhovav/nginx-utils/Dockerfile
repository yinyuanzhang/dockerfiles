FROM obukhovav/ubuntu-utils
MAINTAINER ObukhovAV "https://github.com/ObukhovAV"

RUN apt-get update 
RUN apt-get install -y nginx
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
