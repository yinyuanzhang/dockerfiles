FROM openjdk:8

# Create the photon directory
RUN mkdir /opt/photon

# Copy the photon jar and the data archive to the photon directory
COPY photon-0.2.7.jar  /opt/photon
COPY data.tar.xz       /opt/photon

WORKDIR /opt/photon

# Untar and cleanup
RUN cd /opt/photon & tar xJf data.tar.xz
RUN cd /opt/photon & chmod +x photon-0.2.7.jar & rm data.tar.xz

EXPOSE 2322

WORKDIR /opt/photon

ENTRYPOINT ["java", "-jar", "photon-0.2.7.jar"]
CMD ["-languages", "fo,en,dk,fr,de,it"]