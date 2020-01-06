FROM python:3.6.5-alpine3.7
MAINTAINER Rémy Greinhofer <remy.greinhofer@requestyoracks.org>

# Install packages.
RUN pip install --no-cache-dir flower==0.9.2 redis==2.10.6

# Expose port.
EXPOSE 5555

# Set the entrypoint.
ENTRYPOINT ["celery", "flower"]
