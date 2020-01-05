#
# This is the build for the SYRAS Systematic Review Document Search API
#   https://hub.docker.com/r/scipilot/syras-doc-api
# It requires SciKit-Learn and Scipi, Numpy etc. which I keep separate as they are very large builds.
#
FROM scipilot/sysrev-assist-scikit:latest

ENV HOME=/app

# Install codebase
RUN mkdir /app
COPY . /app/sysrev-assist-python

# Install remaining Python deps (could use requirements.txt - but SKL/Scikit didn't work that way)
RUN pip install "connexion>=1.1,<2" && \
    pip install Flask==0.12 && \
    pip install Flask-RESTful==0.3 && \
    pip install jsonschema==2.6 && \
    pip install PyYAML==3.12 && \
    pip install swagger-spec-validator==2.1 && \
    pip install urllib3==1.22 && \
    pip install Werkzeug==0.14

# Run the Swagger Flask REST server
WORKDIR /app/sysrev-assist-python/python-flask-server-generated
CMD python3 -m swagger_server
