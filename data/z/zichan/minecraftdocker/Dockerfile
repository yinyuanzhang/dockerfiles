FROM java:8 
RUN cd /usr/local;wget http://mcmyadmin.com/Downloads/etc.zip;unzip etc.zip; rm etc.zip

RUN mkdir ~/McMyAdmin;cd ~/McMyAdmin;wget http://mcmyadmin.com/Downloads/MCMA2_glibc26_2.zip;unzip MCMA2_glibc26_2.zip;rm MCMA2_glibc26_2.zip;./MCMA2_Linux_x86_64 -configonly -nonotice -setpass 'burritos';

ADD start.sh /start.sh

RUN sed -i '/Java.Memory=1024/c\Java.Memory=4096' /root/McMyAdmin/McMyAdmin.conf

VOLUME ["/root/McMyAdmin/Minecraft"]
EXPOSE 25565
EXPOSE 8080

CMD /start.sh
