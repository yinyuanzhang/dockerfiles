FROM jacekmarchwicki/android:ubuntu-16-04-java7-8

RUN apt-get update && apt-get install -y fdroidserver
ADD update.py /usr/lib/python2.7/dist-packages/fdroidserver/update.py