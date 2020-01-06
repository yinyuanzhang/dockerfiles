FROM debian:buster-slim

RUN apt-get update && apt-get install -y stress moreutils iperf


RUN echo '#!/bin/sh\n\
cpustressmax=${BUBLA_MAXCPU:-3}\n\ 
iostressmax=${BUBLA_MAXIO:-128}\n\ 
vmstressmax=${BUBLA_MAXMEM:-128}\n\ 
stresstimemax=${BUBLA_MAXSTRESSTIME:-5}\n\ 
sleeptimemax=${BUBLA_MAXSLEEPTIME:-1200}\n\
iperfserverhost=${BUBLA_IPERFSERVERHOST:-speedtest.wtnet.de}\n\ 
iperfserverport=${BUBLA_IPERFSERVERPORT:-5207}\n\ 
while getopts 'c:i:h:m:l:p:s:' opt; do\n\
  case "$opt" in\n\
    c)\n\
      cpustressmax=$OPTARG\n\
      ;;\n\
    i)\n\
      iostressmax=$OPTARG\n\
      ;;\n\
    h)\n\
      iperfserverhost=$OPTARG\n\
      ;;\n\
    m)\n\
      vmstressmax=$OPTARG\n\
      ;;\n\
    l)\n\
      stresstimemax=$OPTARG\n\
      ;;\n\
    p)\n\
      iperfserverport=$OPTARG\n\ 
      ;;\n\
    s)\n\
      sleeptimemax=$OPTARG\n\ 
      ;;\n\
  esac\n\
done\n\
echo "INIT PARAM: max CPU stress\t $cpustressmax "\n\
echo "INIT PARAM: max IO stress\t $iostressmax "\n\
echo "INIT PARAM: max MEM stress\t $vmstressmax "\n\
echo "INIT PARAM: stress TIME max\t $stresstimemax "\n\
echo "INIT PARAM: sleep TIME max\t $sleeptimemax "\n\
echo "INIT PARAM: iperf server \t $iperfserverhost:$iperfserverport "\n\
while :\n\
do\n\
  echo "infinite loops stress and release [ hit CTRL+C to stop]"\n\
  stresstime=$(shuf -i 1-$stresstimemax -n 1)\n\
  cpustress=$(shuf -i 1-$cpustressmax -n 1)\n\
  iostress=$(shuf -i 1-$iostressmax -n 1)\n\
  vmstress=$(shuf -i 1-$vmstressmax -n 1)\n\
  echo stress $cpustress cpu, $iostress io, $vmstress mem, for $stresstime sec | ts\n\
  stress -c $cpustress -i $iostress -m $vmstress -t $stresstime\n\
  echo iperf -c $iperfserverhost -p $iperfserverport -t $stresstime -b 10M -u | ts\n\
  iperf -c $iperfserverhost -p $iperfserverport -t $stresstime -b 10M -u\n\
  sleeptime=$(shuf -i 1-$sleeptimemax -n 1)\n\
  echo sleep for $sleeptime sec | ts\n\
  sleep $sleeptime\n\
done' >> /bin/bubla.sh

RUN chmod a+x /bin/bubla.sh

RUN useradd -u 501 -m -g root bubla && chown -R bubla:root /home/bubla && chmod 744 /home/bubla 

USER 501

WORKDIR /home/bubla 

ENTRYPOINT ["/bin/bubla.sh"]