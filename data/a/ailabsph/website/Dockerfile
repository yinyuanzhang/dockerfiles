FROM ailabsph/website:latest as website

FROM python:3.6.5
WORKDIR /usr/src/app
EXPOSE 8000

# Install vim
RUN apt-get update && \
    apt-get install vim -y

# To copy existing python packages commands
COPY --from=website /usr/local/bin/. /usr/local/bin/.

# To copy existing python packages
COPY --from=website /usr/local/lib/python3.6/site-packages/. /usr/local/lib/python3.6/site-packages/.

# COPY locale locale
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# To copy existing migration files
COPY --from=website /usr/src/app/. .

COPY . .
RUN timeout 30 yes | python manage.py makemigrations

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
