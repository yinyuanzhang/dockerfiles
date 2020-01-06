FROM cytomineuliege/software-python3-base:v2.2.0-py3.6.8

# Install Java
RUN apt-get update && apt-get install openjdk-8-jdk -y && apt-get clean

# Install Neubias-W5-Utilities (annotation exporter, compute metrics, helpers,...)
RUN git clone https://github.com/Neubias-WG5/neubiaswg5-utilities.git
RUN chmod +x /neubiaswg5-utilities/bin/*
RUN cp /neubiaswg5-utilities/bin/* /usr/bin/
RUN cd /neubiaswg5-utilities/ && pip install .
RUN rm -r /neubiaswg5-utilities

# keep re-install of numpy as long as this is open: https://github.com/scikit-image/scikit-image/issues/3586
# latest scikit-image is incompatible with latest numpy (1.16) on pip. This is being fixed by skimage team.
RUN pip install numpy==1.15.4
