FROM ppodgorsek/robot-framework:latest

ENV PYYAML_VERSION 5.1
ENV PABOT_VERSION 0.62
ENV ROBOTFRAMEWORK_VERSION 3.1.2
ENV ROBOTFRAMEWORK_DATADRIVER_VERSION 0.0.8

RUN pip3 install \
  --no-cache-dir \
  robotframework>=${ROBOTFRAMEWORK_VERSION} \
  pyyaml>=${PYYAML_VERSION} \
  robotframework-pabot>=${PABOT_VERSION} \
  robotframework-datadriver>=${ROBOTFRAMEWORK_DATADRIVER_VERSION}

