FROM java:8  
COPY . /var/www/java  
WORKDIR /var/www/java  
RUN javac StdOut.java  
CMD ["java", "StdOut >> /var/log/test.log"]  
