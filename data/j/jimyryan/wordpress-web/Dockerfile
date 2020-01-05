# Debian
FROM nginx:latest 
MAINTAINER JimyRyan

#################################################################################
#################################################################################
#                                                                               #
#                [START :: TIMEZONE, LOCALE & UPDATE / UPGRADE]                 #
#                                                                               #
#################################################################################

RUN apt-get update -y \
    && apt-get install -y locales

# Set locale and timezone 
ENV LANGUAGE fr_FR.UTF-8
ENV LANG fr_FR.UTF-8
ENV LC_ALL fr_FR.UTF-8
ENV TZ Europe/Paris

# Change locale and timezone 
RUN set -x \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && sed -i -e 's/# '$LANG' UTF-8/'$LANG' UTF-8/' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=$LANG \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Update distribution
RUN apt-get update \
    && apt-get upgrade -y

#################################################################################
#                                                                               #
#                   [END :: TIMEZONE, LOCALE & UPDATE / UPGRADE]                #
#                                                                               #
#################################################################################
#################################################################################

  
# nginx config
ENV NGINX_MAIN_DOMAIN example.com
ENV NGINX_DOMAINS_STRING_PARAM www.example.com example.com

# Copy all nginx config files
# Note from Docker doc (https://docs.docker.com/engine/reference/builder/#add)
# > If <src> is a directory, the entire contents of the directory are copied, including filesystem metadata.
# > Note: The directory itself is not copied, just its contents.
ADD data/etc/nginx /etc/nginx/

# Delete the default config file
# Change the file extention ".conf" to ".conf.template"
RUN set -e \
	&& rm -rf /etc/nginx/conf.d/default.conf \
	&& for file in /etc/nginx/conf.d/*.conf; do mv "$file" "$file.template"; done

# Copy the startup script
COPY data/config-and-start.sh /opt/

# Apply good right
RUN set -e \
	&& chmod u+x /opt/config-and-start.sh \
	&& chmod -R 644 /etc/nginx/*
	
CMD /opt/config-and-start.sh
