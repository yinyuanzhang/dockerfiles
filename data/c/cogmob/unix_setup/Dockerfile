from ubuntu:latest
run apt-get update
run apt-get -y install sudo
run useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
copy . /root/unix_setup
run /root/unix_setup/ubuntu_install_super.sh
run /root/unix_setup/ubuntu_install.sh
run mkdir /root/volume
run mkdir ~/.ssh
env NOTVISIBLE "in users profile"
expose 22
run /usr/sbin/sshd
