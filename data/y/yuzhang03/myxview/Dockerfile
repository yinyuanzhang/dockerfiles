# Build from a recent python3 version (64 bit python required for Tensorflow)
FROM python:3.6.5-onbuild
COPY requirements.txt requirements.txt

# Install required python modules
RUN pip3 install -r requirements.txt

# An RGB input image for local debug/testing
# Move it to the root dir where inference code (and tutorial) expects to find it
#RUN mv 1047.tif /1047.tif

# Rename the trained checkpoint from the baseline model release to `model.pb`
# so that the `run.sh` file will find and use it
#RUN mv vanilla.pb model.pb
# Note: you can swap in one of your own checkpoints instead, just change the line above
