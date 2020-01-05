FROM redash/base:latest

# We first copy only the requirements file, to avoid rebuilding on every file
# change.
WORKDIR /app
RUN git clone https://github.com/getredash/redash.git
RUN mv redash redash.bak
RUN cp -r redash.bak/* ./
# COPY requirements.txt requirements_dev.txt requirements_all_ds.txt ./
RUN pip install -r requirements.txt -r requirements_dev.txt -r requirements_all_ds.txt

COPY . ./
RUN npm install && npm run build && rm -rf node_modules
RUN chown -R redash /app
USER redash

ENTRYPOINT ["/app/bin/docker-entrypoint"]
CMD ["server"]