FROM appium/appium

# RUN apt-get update && apt-get install -y openssh-server
# RUN useradd -ms /bin/bash adbuser
# USER adbuser

# Install AWS
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y netcat
RUN pip install awscli --upgrade --user
ENV S3_BUCKET_URL s3://emulator-screencap
ENV AWS_ACCESS_KEY_ID=AKIAJHYF3O66YFLVQDEQ
ENV AWS_SECRET_ACCESS_KEY=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
ENV PATH="~/.local/bin:${PATH}"

ENV APPIUM_LOG_LEVEL=warn

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22


RUN mkdir /app
ADD apk/WhatsApp.apk /app/WhatsApp.apk

ENV REMOTE_ADB=True
# ENV ANDROID_DEVICES=phone:5555

RUN mkdir /server
COPY . /server

WORKDIR /server
RUN npm install
# RUN npm install -g sqlite3 
# RUN npm install sqlite3 --build-from-source

RUN npm install pm2 -g

# Connect papertrail to pm2
# ENV PAPERTRAIL_HOST=logs2.papertrailapp.com
# ENV PAPERTRAIL_PORT=13889
# RUN pm2 install pm2-papertrail
# RUN pm2 set pm2-papertrail:host $PAPERTRAIL_HOST
# RUN pm2 set pm2-papertrail:port $PAPERTRAIL_PORT
# Redirect PM2 logs to stdout and sterr


COPY ./files/entry_point.sh /root/entry_point.sh
RUN chmod u+x /root/entry_point.sh
CMD /root/entry_point.sh

# CMD service ssh restart && /root/entry_point.sh
# CMD ["service", "ssh", "restart","&&","/root/entry_point.sh"]