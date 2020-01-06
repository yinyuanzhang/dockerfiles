FROM opensciencegrid/osgvo-tensorflow-gpu

MAINTAINER Edgar Fajardo <emfajard@ucsd.edu>

RUN pip --no-cache-dir install \
        astropy \
        && \
    python -m ipykernel.kernelspec


RUN pip3 --no-cache-dir install \
         astropy \
         && \
    python3 -m ipykernel.kernelspec

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt