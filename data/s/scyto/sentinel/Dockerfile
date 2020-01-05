# Use frovlad/alpine-glibc image (glibc is needed)
FROM frolvlad/alpine-glibc

# Copy the current directory contents into the container at /app
COPY hdsentinel.sh .

# Install any needed packages and do needed file system modifcations
RUN apk add --no-cache wget \
	&& wget https://www.hdsentinel.com/hdslin/hdsentinel-017-x64.gz \
	&& gunzip hdsentinel-017-x64.gz \
	&& apk del wget \
	&& chmod 0755 hdsentinel-017-x64 \
	&& mkdir /etc/hdsentinel\
    	&& mv hdsentinel-017-x64 /bin/hdsentinel \
	&& chmod +x hdsentinel.sh \
	&& echo "*/10       *       *       *       *       hdsentinel -r /etc/hdsentinel/hdsreport.html -html" >> /var/spool/cron/crontabs/root

# Define environment variable
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV LANG C.UTF-8

# Run  when the container launches 
ENTRYPOINT ["./hdsentinel.sh"]
