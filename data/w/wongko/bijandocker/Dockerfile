#pertama pull base image yang kita inginkan (biasanya OS tertentu)
FROM wongko/ubuntu-kosong:latest

#credit pembuat image ini
MAINTAINER panji iman baskoro <panjidia995@gmail.com>
MAINTAINER bijan docker <bijandocker@gmail.com>

#memulai/Menjalankan proses installasi aplikasi yang diinginkan 
RUN apt-get update && apt-get install apache2 -y

#menjalankan service dan perintah yang diberikan
CMD service apache2 restart && /bin/bash
