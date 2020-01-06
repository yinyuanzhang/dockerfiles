
# Use an official Python runtime as a parent image
FROM python:latest

# Set working director
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this computer
EXPOSE 80

# run app.py when container launches
CMD ["python", "app.py"]