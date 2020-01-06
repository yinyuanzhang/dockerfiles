# Start with Keras base image
FROM kaixhin/keras

RUN pip install --upgrade pip
RUN pip install -U scikit-learn
RUN pip install jupyter

RUN apt-get update && apt-get install -y vim

# Expose port
EXPOSE 80
EXPOSE 8080
EXPOSE 8888

# Set working directory
WORKDIR /root