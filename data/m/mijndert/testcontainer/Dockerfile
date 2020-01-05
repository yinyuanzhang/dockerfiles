FROM node
LABEL maintainer Mijndert Stuij "mijndert@mijndertstuij.nl"

RUN apt-get update && \
    apt-get install -y python-pip zip && \
    pip install awscli && \
    pip install ansible && \
    pip install boto3 && \
    pip install botocore && \
    npm install -g eslint && \
    npm install -g babel-eslint && \
    npm install -g eslint-plugin-babel && \
    npm install -g eslint-plugin-react && \
    npm install -g eslint-plugin-import && \
    npm install -g eslint-config-airbnb && \
    npm install -g eslint-plugin-jsx-a11y
    
RUN rm -rf /var/lib/apt/lists/*