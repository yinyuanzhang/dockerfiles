FROM ubuntu:latest

# Install
#RUN apk add --no-cache unrar cksfv bash cfv p7zip-full p7zip-rar
RUN apt-get update
RUN apt-get install -y cfv cksfv p7zip-full p7zip-rar unrar file
# Build
WORKDIR /src/
COPY . /src/
RUN cd /src

ENV CLEANMODE none
ENV DELAY 900

# Start the script
CMD ["bash", "./unrar-script.sh"]
