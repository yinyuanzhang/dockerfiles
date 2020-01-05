FROM aibakevision/object-detector-base-gpu:cuda8.0-ubuntu16.04-python3.5.2

# Make workspace
RUN mkdir /workspace/webapp
ADD entrypoint.sh /workspace/webapp
ADD ./src /workspace/webapp
WORKDIR /workspace/webapp

# Install dependencies of python application
RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 5001
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]


