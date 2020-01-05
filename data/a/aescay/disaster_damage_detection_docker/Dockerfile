# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

# Set labels for documentation and organization purposes
LABEL maintainer="Andrew Escay <andrew.escay@gmail.com>"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN conda install jupyter -y && \
    conda clean -y -all

# Make port 80 available to the world outside this container
EXPOSE 9999

VOLUME /app

# Define environment variable
ENV name=disaster_damage_detection

# Run app.py when the container launches
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
