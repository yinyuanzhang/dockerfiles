FROM sambritton/cuda-10.1-base
FROM sambritton/cuda-10.1-base
RUN # Update list of available packages, then upgrade them
RUN apt-get update -y
RUN apt-get update
RUN apt-get install -y cmake
RUN apt-get install -y vim
RUN apt-get install -y git
CMD exec /bin/bash "$@"
