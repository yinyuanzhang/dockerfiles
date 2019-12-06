# A Dockerfile for running the Open Modeling Framework
# Tested on 2018-11-08 with Docker Version 18.06.1-ce-mac73 (26764)
FROM ubuntu:16.04
LABEL maintainer="<david.pinney@nreca.coop>"

# Install and setup OMF reqs
RUN apt-get -y update && apt-get install -y python sudo vim
WORKDIR /home/omf
COPY install.py .
COPY requirements.txt .
COPY setup.py .
# Only re-run the environment installation if install.py, requirements.txt, or setup.py changed (takes a long time)
RUN python install.py
# Unfortunately, these instructions must be here to invalidate the build cache in case any file in the OMF changes. The root cause is the use of
# non-absolute package version numbers in requirements.txt
WORKDIR /home/omf/omf
COPY omf .
# Install requirements with pip again because 1) install.py doesn't do everything for some reason and 2) it's necessary due to the use of non-absolute
# package version numbers
WORKDIR /home/omf
RUN pip install -r requirements.txt
# Copy in all needed source code
WORKDIR /home/omf/omf
#COPY omf .
COPY omf/scratch/GRIP/grip.py .
COPY omf/scratch/GRIP/grip_config.py .
ENTRYPOINT ["python"]
CMD ["-m", "grip"]