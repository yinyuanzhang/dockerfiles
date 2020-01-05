FROM java:8
EXPOSE 8080

# Add resources
ADD aider-*.jar backend.jar
ADD wait-for-db.sh wait-for-db.sh
ADD products.csv products.csv

# Install mysql-client
RUN apt-get update; apt-get install -y mysql-client

# Wait for database to be up 
RUN chmod +x wait-for-db.sh
ENTRYPOINT ["./wait-for-db.sh"]
