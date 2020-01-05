# Use an official Python runtime as a parent image
FROM pytorch/pytorch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# RUN pip install https://download.pytorch.org/whl/cu90/torch-1.0.1-cp36-cp36m-win_amd64.whl

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "test.py"]