FROM aibakevision/object-detector-base-gpu:cuda8.0-ubuntu16.04-python3.5.2

RUN apt-get install -y awscli

# Make workspace
ADD ./src /workspace
WORKDIR /workspace
RUN mkdir /workspace/output
RUN mkdir /workspace/output/final

# Set aws config file path
ARG aws_config_file=/workspace/.aws/config
ENV AWS_CONFIG_FILE=${aws_config_file}
RUN echo $AWS_CONFIG_FILE

# Download dataset
ARG s3_dataset_path=s3://aibakevision-object-detection/darknet/dataset
RUN aws s3 sync ${s3_dataset_path} /workspace/dataset

# Convert Crested Gecko dataset based on Pascal VOC to Darknet format
RUN python cg_label.py

# Run trainning and upload trained weight
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]


