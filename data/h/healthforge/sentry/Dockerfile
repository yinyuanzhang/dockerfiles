FROM sentry:9.1
RUN PSYCOPG=$(pip freeze | grep psycopg2) \
	&& pip uninstall -y $PSYCOPG \
	&& pip install --no-binary :all: $PSYCOPG

