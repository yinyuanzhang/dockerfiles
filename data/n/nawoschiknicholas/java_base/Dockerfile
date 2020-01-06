FROM ibmjava:8-jre

# Update the program cache and install needed programs
RUN apt-get update -y && \
        apt-get install -y wget unzip

# Add appuser for run
RUN groupadd -g 777 appuser
RUN useradd -r -u 777 -g appuser appuser

# Make entrypoint folder
RUN mkdir /entrypoint

# Set permissions for folders
RUN chmod 777 /opt
RUN chmod 777 /entrypoint
RUN chmod 777 /tmp
RUN chmod 777 /var/lib
RUN chmod 777 /home