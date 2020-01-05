FROM ubuntu:18.04
LABEL maintainer="pascal.hebbeker@gmail.com"
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git gfortran fftw3-dev locate make
RUN updatedb

CMD chmod +x /molsim/pull_tools/run_tests.sh && cd /molsim/ && ./pull_tools/run_tests.sh
