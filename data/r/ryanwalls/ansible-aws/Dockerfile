FROM generik/ansible:v2.2.1.0-1

ADD https://storage.googleapis.com/kubernetes-release/release/v1.11.0/bin/linux/amd64/kubectl /usr/bin/
RUN chmod +x /usr/bin/kubectl
RUN pip install boto3
RUN pip install awscli==1.11.43
