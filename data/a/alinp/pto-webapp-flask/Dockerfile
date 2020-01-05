# Dockerfile-flask

FROM python:3.6
RUN mkdir /app
WORKDIR /app
# Expose the port uWSGI will listen on
EXPOSE 5000
# Copy the requirements file in order to install
# Python dependencies and install them
COPY requirements.txt .
RUN pip install -r requirements.txt
# We copy the rest of the codebase into the image
COPY app.ini .
COPY mw/ .
# Finally, we run uWSGI with the ini file
CMD uwsgi --ini app.ini