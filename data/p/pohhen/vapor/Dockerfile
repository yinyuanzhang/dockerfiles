# Use version tag to avoid unwanted changes
FROM        swift:4.2
# Create user Vapor-user
RUN         useradd -m vapor
# Make the app folder
RUN         mkdir -p /app
RUN         chown vapor:vapor /app
# Set working directory, all files copies here
WORKDIR     /app
COPY        apt-vapor.sh /app/
# Vapor repository add from http://apt.vapor.sh
RUN         bash ./apt-vapor.sh
# Install Vapor from added source
RUN         apt-get install -y vapor
# Switch to non-root user
USER        vapor
# Build and run vapor, use CDM since it can be overwritten in command line
CMD [ "bash", "-c", "vapor build --clean --run" ]
