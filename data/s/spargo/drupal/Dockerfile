FROM "spargo/php:latest"

# Copy Scripts
COPY --chown=root:root ./_scripts/ /
RUN chmod 540 -R /spargo/build
RUN /spargo/build/00-additions.sh && \
    /spargo/build/00-create_user.sh

# Copy Drupal Site
COPY --chown=drupal:apache ./_site/ /
WORKDIR /spargo/drupal
RUN /spargo/build/00-install_drupal.sh 

# Clean up
RUN rm -rf /spargo/build

ENV DRUSH_PHP=/usr/bin/php
