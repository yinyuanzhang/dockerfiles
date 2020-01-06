FROM kahinf/ubuntu:latest

# Copy the application source the /app directory
ADD . /app
 
# Produce a ready-to-run container
RUN /app/container/compile.sh

EXPOSE 3306