FROM mariadb:latest
MAINTAINER okazakiyuji
# Trac の hotcopyの出力結果をSVNに保存しやすくするために、
# mysqldumpで日付などでないように、1レコードは1行で出力します
ADD kanon.cnf /etc/mysql/conf.d/

