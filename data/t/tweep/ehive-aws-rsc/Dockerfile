# Container 'lineage' 
#  tweep/ehve-base-ubuntu-18
#            ↓
# tweep/ehve-base-ubuntu-18-extended  


# DOCKERFILE: ehive-aws-rsc/latest 

FROM tweep/ehive-base-ubuntu-18-extended:latest

RUN groupadd -g 2000 ugroup
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g ugroup -G sudo -u 1000 ubuntu

# Declare default nvironment variables for AWS CLI and confd
ENV AWS_DEFAULT_OUTPUT="json"
ENV AWS_DEFAULT_REGION="us-west-2"



# Install AWS CLI to submit jobs from witin this container
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y vim awscli cpanminus build-essential 
RUN cpanm -v AWS::CLIWrapper String::Random Switch

#set root password
RUN echo "root:docker" | chpasswd

# Apply latest EnsEMBL eHive patch
COPY patch_2019-01-24.mysql /repo/ensembl-hive/sql/patch_2019-01-24.mysql 

# Copy Madhu's latest AWS 
COPY AWSBatch.pm /repo/ensembl-hive/modules/Bio/EnsEMBL/Hive/Meadow/AWSBatch.pm

# Copy AWS Batch meadow tests
COPY awsbatch.t /repo/ensembl-hive/t/04.meadow/awsbatch.t

# Copy hive config which has AWS Batch meadow configurations
COPY hive_config.json /repo/ensembl-hive/hive_config.json

COPY set_ehive_env.sh /


USER ubuntu
WORKDIR /home/ubuntu

ENTRYPOINT [ "/repo/ensembl-hive/scripts/dev/simple_init.py" ]
CMD [ "/bin/bash" ]


