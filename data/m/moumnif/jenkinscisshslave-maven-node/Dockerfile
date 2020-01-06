FROM jenkinsci/ssh-slave

# Update et installation des misc 
RUN apt-get update -y
RUN apt-get install curl wget -y

# Upgrade de openjdk8 (la version présente dans jenkinsci/ssh-slave pose un soucis à l'execution de Maven)
RUN apt-get install --only-upgrade openjdk-8-jdk -y

# Installation de Maven
RUN apt-get install maven -y

# Installation de nodejs et npm
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install nodejs -y

# Installation de angular cli
RUN npm install -g @angular/cli

# Installation de node-sass (besoin d'un accès à Github)
RUN mkdir /node-sass && cd /node-sass && wget https://github.com/sass/node-sass/releases/download/v4.11.0/linux-x64-64_binding.node