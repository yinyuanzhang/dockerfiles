FROM labshare/base:latest

# Set the source folder
ARG SOURCE_FOLDER="./"

WORKDIR "/tomojs"

# Copy the contents of the source folder into the image
COPY ${SOURCE_FOLDER} .

# Rebuild native node_modules
RUN npm rebuild

# Run the service using pm2 and the shortcut
ENTRYPOINT ["pm2-runtime", "ecosystem.config.js", "--env", "production"]

EXPOSE 8000

