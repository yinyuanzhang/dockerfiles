from ubuntu
run apt-get update -y
run apt-get install -y apache2
expose 80 
cmd ["usr/sbin/apache2ctl","-D","FOREGROUND"]
