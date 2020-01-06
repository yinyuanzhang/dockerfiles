FROM rezenders/armv7hf-ubuntu-openjdk-ros:8-jdk-bionic 

RUN apt-get update && apt-get install -y \
    ros-melodic-mavros \
    && rm -rf /var/lib/apt/lists/

RUN wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
RUN chmod a+x install_geographiclib_datasets.sh
RUN ./install_geographiclib_datasets.sh

COPY launch /launch
