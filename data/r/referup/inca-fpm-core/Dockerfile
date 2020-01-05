FROM referup/inca-fpm

RUN test -d /root/.drush/cache/download && test $(ls /root/.drush/cache/download/ | wc -l) -gt 0 && rm -vfr /root/.drush/cache/download/* || echo "Drush Download Cache empty"
RUN test $(ls /var/www/html/ | wc -l) -eq 0 && echo "path /var/www/html/ it's empty" || rm -vfr /var/www/html/*

COPY files/talentclue.make /tmp
COPY files/patch_log_sanitized_keys_error_log.patch /var/www/html
COPY files/ATS-4995-fix-file_create_filename-performance.patch /var/www/html
COPY files/ATS-5138-drupal-core-patch-avoid-locale-cache-stampede-on-core-deployment.patch /var/www/html
RUN drush --verbose make -y --no-cache /tmp/talentclue.make
COPY files/robots.txt /var/www/html
