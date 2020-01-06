FROM alpine:3.10.2

WORKDIR /root/

#安装所需要的wget
RUN apk --no-cache add bash wget tzdata;

#添加经过修改的安装脚本
ADD ssr-install.sh ssr-install.sh
#这是管理脚本
ADD ssr.sh ssr.sh

#添加执行权限
RUN chmod u+rwx ssr.sh;chmod u+rwx ssr-install.sh


#--------------- 初始设置 ---------------

#初始端口 整数
#ENV init_port 8000

#初始密码 文本
#ENV init_password psw

#设置加密方式
#1.none
#Tip: 如果使用 auth_chain_a 协议，请加密方式选择 none，混淆随意(建议 plain)
#2.rc4
#3.rc4-md5
#4.rc4-md5-6
#5.aes-128-ctr
#6.aes-192-ctr
#7.aes-256-ctr
#8.aes-128-cfb
#9.aes-192-cfb
#10.aes-256-cfb
#11.aes-128-cfb8
#12.aes-192-cfb8
#13.aes-256-cfb8
#14.salsa20
#15.chacha20
#16.chacha20-ietf
#Tip: salsa20/chacha20-*系列加密方式，需要额外安装依赖 libsodium ，否则会无法启动ShadowsocksR !" && echo
#ENV init_method 5

#设置ssr协议
#1.origin
#2.auth_sha1_v4
#3.auth_aes128_md5
#4.auth_aes128_sha1
#5.auth_chain_a
#6.auth_chain_b
#ENV init_protocol 3

#是否兼容原版
#ENV protocol_compatible n

#协议参数 - 单个端口设备数
#auth_* 系列协议 不兼容原版才有效
#ENV protocol_param 32

#混淆插件
#1.plain
#2.http_simple
#3.http_post
#4.random_head
#5.tls1.2_ticket_auth
#Tip: 如果使用 ShadowsocksR 加速游戏，请选择 混淆兼容原版或 plain 混淆，然后客户端选择 plain，否则会增加延迟 !
#另外, 如果你选择了 tls1.2_ticket_auth，那么客户端可以选择 tls1.2_ticket_fastauth，这样即能伪装又不会增加延迟 !
#如果你是在日本、美国等热门地区搭建，那么选择 plain 混淆可能被墙几率更低 !
#ENV obfs 5

#是否兼容原版
#ENV obfs_compatible n

#设置单个端口限速(KB/s)
#ENV speed_limit_maxConn 0 

#设置单个端口最大总速度
#ENV speed_limit_maxUser 0

#执行安装脚本
RUN ./ssr-install.sh \
                    #初始端口 1
                    ${init_port}           \ 
                    #初始密码 2
                    ${init_password}       \
                    #初始加密方式 3
                    ${init_method}         \
                    #ssr协议 4
                    ${init_protocol}       \
                    #ssr协议是否兼容原版 5
                    ${protocol_compatible} \
                    #混淆设置 6
                    ${obfs}                \
                    #是否兼容原版 7
                    ${obfs_compatible}     \
                    #协议参数 8
                    ${protocol_param}      \
                    #单端口最大连接速度 9
                    ${speed_limit_maxConn} \
                    #单端口最大总速度 10
                    ${speed_limit_maxUser}

#覆盖掉旧的管理脚本
ADD ssr.init.d /etc/init.d/ssr
#设置启动命令
CMD /bin/bash /etc/init.d/ssr start && /bin/bash --login
