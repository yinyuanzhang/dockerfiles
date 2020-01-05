# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Oracle
RUN apt-get update --fix-missing
RUN apt-get install -y build-essential --force-yes
RUN apt-get install -y libaio1 --force-yes
RUN apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev --force-yes

WORKDIR /app

ADD requirement.txt /app
RUN pip install -r requirement.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 80 available to the world outside this container
EXPOSE 5000

# ENV TNS_ADMIN=/app/oracletns
ENV ORACLE_HOME=/oracle64
ENV LD_LIBRARY_PATH=/oraclelib:$LD_LIBRARY_PATH


# Run app.py when the container launches
CMD ["bash", "run.bash"]