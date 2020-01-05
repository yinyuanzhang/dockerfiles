FROM python:3.6.4-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    python3-dev \
    apache2 \
    apache2-dev \
    gcc \
    # HTTPS setup https://certbot.eff.org/lets-encrypt/pip-apache \
    curl \
    && curl https://dl.eff.org/certbot-auto > /usr/local/bin/certbot-auto && chmod a+x /usr/local/bin/certbot-auto \
    && certbot-auto -n --os-packages-only \
    && pip install --upgrade pip \
    && pip install virtualenv>=15.* \
    && pip install mod_wsgi \
    && virtualenv -q -p /usr/local/bin/python3.6 /srv/env \
    && rm -rf /var/lib/apt/

RUN mkdir -p /etc/apache2/modules/ && ln -s /usr/local/lib/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so /etc/apache2/modules/mod_wsgi.so

RUN echo "LoadModule wsgi_module /etc/apache2/modules/mod_wsgi.so" > /etc/apache2/mods-available/wsgi.load \
    && touch /etc/apache2/mods-available/wsgi.conf \
    && ln -s /etc/apache2/mods-available/wsgi.* /etc/apache2/mods-enabled/

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000
EXPOSE 80
EXPOSE 443

# Define environment variable

# Run app.py when the container launches
# CMD ["python", "-u", "manage.py", "runserver"]
#ENTRYPOINT ["/bin/bash", "./start.sh"]
