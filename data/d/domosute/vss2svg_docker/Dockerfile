FROM ubuntu:16.04
# Update and install necessary dependency for libvisio2svg
RUN apt-get update && \
apt-get install -y git wget cmake unzip && \
apt-get install -y libpng-dev libiconv-hook-dev libfreetype6-dev libfontconfig1-dev librevenge-dev libvisio-dev libxml2-dev libwmf-dev
# Compile libemf2svg which is required for libvisio2svg
RUN mkdir /opt/docker_bld && \
cd /opt/docker_bld && \
git clone https://github.com/kakwa/libemf2svg && \
cd /opt/docker_bld/libemf2svg && \
cmake . && \
make && \
make install
# Now compile libvisio2svg
RUN cd /opt/docker_bld && \
git clone https://github.com/kakwa/libvisio2svg && \
cd /opt/docker_bld/libvisio2svg && \
cmake . && \
make && \
make install
# Update libraries
RUN ldconfig

CMD [bash]
