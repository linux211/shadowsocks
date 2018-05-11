导语：
世界上有些东西，你可以看不到，也摸不着，但不能否定其存在。当想你想下载苹果的一个操作系统时，当你想看一篇关于叙利亚的文章时，当你想用google搜索“温”时候，你发现你打不开网站，不是因为网站服务器出了问题，而是你硬生生地撞到了墙上，这堵墙也就是“GFW”。身处的”互联网”的我们，也不过是一堵墙内上个局域网罢了。

翻墙梯子
所谓“授人以鱼不如授人以渔”，与其去购买一个不太稳定的VPN，还不如普及一下如何搭建属于自己的梯子，翻过这堵墙看看外面的新世界！

准备工作
1.能够上外网的服务器
2.快速搭建梯子的脚本
3.连接梯子的客户端

实战说明
1.购买阿里云或者国内其他厂商的云服务器，不过和普通服务器不一样的是需要是境外的服务器。
2.执行Shadowsocks-libev搭建脚本（具体见文章结尾）。
3.配置Shadowsocks客户端，具体可以见下文提供的模板。
4.脚本适用于CentOS6和CentOS7，内存要求大于128M。

服务端具体步骤
1.在任意路径，下载一键安装脚本shadowsocks-libev
2.解压shadowsocks-libev.zip压缩包后，会有一个shadowsocks-libev.sh的文件，赋予文件脚本执行权限，chmod a+x shadowsocks-libev.sh
3.执行脚本，./shadowsocks-libev.sh 2>&1 | tee shadowsocks-libev.log
安装过程中后，会有以下提示
Congratulations, shadowsocks-libev install completed!
Your Server IP:your_server_ip
Your Server Port:your_server_port
Your Password:your_password
根据自身的情况依次填写，具体实例
Your Local IP:127.0.0.1
Your Local Port:8989
Your Encryption Method:aes-256-gcm（默认是aes-256-gcm加密协议）
最后成功后可以看到以下字样
Welcome to new world
Enjoy it!

客户端配置实例
根据自身的系统情况，下载不同的客户端，具体下载客户端SSR地址如下
https://github.com/shadowsocks

详细Windows客户端配置如下

《轻松搭建翻墙神器Shadowsocks》

Tips：
如果是Windows系统的话，需要安装.Net工具，根据安装不同的版本的.Net工具，启动客户端

最后
welcome to new world！
