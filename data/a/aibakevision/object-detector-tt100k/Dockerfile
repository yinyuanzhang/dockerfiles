FROM aibakevision/object-detector-tt100k-base-gpu:cuda8.0-ubuntu16.04-python2.7.12

# Install awscli,..
#RUN apt-get install -y awscli python-tk

# Make workspace
# For tsinghua-tencent 100k
RUN mkdir /workspace/tt100k/data
RUN mkdir /workspace/tt100k/weights

# For Webapp 
RUN mkdir /workspace/webapp
ADD entrypoint.sh /workspace/webapp
ADD ./src /workspace/webapp
WORKDIR /workspace/webapp

# Set aws config file path
ARG aws_config_file=/workspace/webapp/.aws/config
ENV AWS_CONFIG_FILE=${aws_config_file}
RUN echo $AWS_CONFIG_FILE

# Download dataset
#ARG s3_data_path=s3://aibakevision-object-detection/caffe/tt100k/data
#RUN aws s3 sync ${s3_data_path} /workspace/tt100k/data

# Download weights
#ARG s3_weights_path=s3://aibakevision-object-detection/caffe/tt100k/weights
#RUN aws s3 sync ${s3_weights_path} /workspace/tt100k/weights

# Install dependencies of python application
#RUN pip install --no-cache-dir werkzeug flask tornado numpy pandas pillow pyyaml opencv-python scikit-image matplotlib
RUN pip install --no-cache-dir protobuf

#EXPOSE 5003
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
#ENTRYPOINT ["/bin/bash"]

