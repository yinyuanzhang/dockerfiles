# Use an official Python runtime as a parent image
FROM python:3.7

WORKDIR /app

# Install any needed packages specified in requirements.txt
ADD requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 4000

# Copy the current directory contents into the container at /app
COPY /src /app


# Run app.py when the container launches
CMD ["python", "app.py"]

