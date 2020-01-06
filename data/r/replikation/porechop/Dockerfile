FROM replikation/debian_basic
MAINTAINER Christian Brandt <christian.jena@gmail.com>
RUN apt-get update
RUN apt-get install -y python3-pkg-resources
RUN git clone https://github.com/rrwick/Porechop.git
WORKDIR /Porechop/
RUN python3 setup.py install
ENTRYPOINT ["porechop"]
CMD ["-h"]
