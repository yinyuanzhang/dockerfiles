FROM blinkreaction/drupal-apache-php:2.2-5.5

# Fix could not open remote debug file.
RUN touch /var/log/xdebug.log; chmod 666 /var/log/xdebug.log
# Disable xdebug by default.
RUN mv /etc/php5/mods-available/xdebug.ini /etc/php5

# Security

## Install ClamAV
RUN apt-get update && apt-get install -y clamav clamav-freshclam
RUN freshclam
