#!/bin/bash
#Date:2019-05-06

source /etc/profile

install_dir=/opt/gumimg/

#公网地址
#url_ip=47.110.40.197
#内网地址
url_ip=172.16.119.60


##修改内核参数
kernel(){
cp /etc/sysctl.conf /etc/sysctl.conf_bak
echo '
    net.ipv4.ip_forward = 1
    net.ipv4.conf.default.accept_source_route = 0
    kernel.sysrq = 0
    kernel.core_uses_pid = 1
    net.bridge.bridge-nf-call-ip6tables = 0
    net.bridge.bridge-nf-call-iptables = 0
    net.bridge.bridge-nf-call-arptables = 0
    kernel.msgmnb = 65536
    kernel.msgmax = 65536
    kernel.shmmax = 68719476736
    kernel.shmall = 4294967296
    vm.swappiness = 0
    net.ipv4.neigh.default.gc_stale_time = 120
    net.ipv4.conf.all.rp_filter = 0
    net.ipv4.conf.default.rp_filter = 0
    net.ipv4.conf.eth0.rp_filter = 0
    net.ipv4.conf.default.arp_announce = 2
    net.ipv4.conf.all.arp_announce = 2
    net.ipv4.tcp_max_tw_buckets = 10000
    net.ipv4.tcp_syncookies = 1
    net.ipv4.tcp_max_syn_backlog = 8096
    net.ipv4.tcp_synack_retries = 2
    net.ipv4.conf.lo.arp_announce = 2
    net.ipv4.tcp_keepalive_time = 1200
    net.ipv4.ip_local_port_range = 10000 65000
    net.ipv4.tcp_syncookies = 1
    net.ipv4.tcp_tw_reuse = 1
    net.ipv4.tcp_tw_recycle = 1
    net.ipv4.tcp_fin_timeout = 30
net.ipv4.ip_local_reserved_ports = 1-9999,11001-11002,10501-10506,10601-10606,27000,16001,22181' > /etc/sysctl.conf
sleep 2
sysctl -p
}
#误删除的配置与基本环境
basics(){
pip_url=http://${url_ip}/download/pip-19.1.tar.gz
setuptools_url=http://${url_ip}/download/setuptools-41.0.1.zip
yum install  -y gcc gcc-c++ make unzip lrzsz wget   epel-release  net-tools
mkdir ${install_dir}
which pip
if [ $? -eq 0 ];then
    cd ${install_dir}
    wget ${pip_url}
    wget ${setuptools_url}
    unzip setuptools-41.0.1.zip
    cd setuptools-41.0.1 && python setup.py  install
    cd ${install_dir}
    tar xf pip-19.1.tar.gz
    cd  pip-19.1 && python setup.py install
    pip install trash-cli
    echo "alias rm='echo The rm command is disabled. Use trash-put'"   >> /etc/bashrc
else
    pip install trash-cli
    echo "alias rm='echo The rm command is disabled. Use trash-put'"   >> /etc/bashrc
fi
}


#安装node版本
node(){
    node_url=http://${url_ip}/download/node-v8.11.1-linux-x64.tar.gz
    cd ${install_dir}
    wget ${node_url}
    tar xf node-v8.11.1-linux-x64.tar.gz  -C /usr/local
}
#安装Java环境
java(){
    jdk_url=http://${url_ip}/download/jdk-8u201-linux-x64.tar.gz
    yum -y install java-devel
    cd ${install_dir}
    wget ${jdk_url}
    tar xf jdk-8u201-linux-x64.tar.gz  -C /usr/local
    manven_url=http://${url_ip}/download/apache-maven-3.6.1-bin.tar.gz
    wget ${manven_url}
    wget http://${url_ip}/download/settings.xml
    tar xf apache-maven-3.6.1-bin.tar.gz -C /usr/local
    cat settings.xml > /usr/local/apache-maven-3.6.1/conf/settings.xml
}
PATH(){
    cp /etc/profile /etc/profile.bak
echo '
NODE_HOME=/usr/local/node-v8.11.1-linux-x64
M2_HOME=/usr/local/apache-maven-3.6.1
JAVA_HOME=/usr/local/jdk1.8.0_201
ANT_HOME=/usr/local/apache-ant-1.9.4
PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH:$ANT_HOME/bin:$M2_HOME/bin:$NODE_HOME/bin
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
export JAVA_HOME JRE_HOME ANT_HOME PATH CLASSPATH ' >> /etc/profile
}


case $1 in
    node_install)
        kernel
        basics
        node
        PATH
    ;;
    java_install)
        kernel
        basics
        java
        PATH
    ;;
    *)
        echo "默认使用内网地址下载文件，参数为(node_install|java_install)"
        exit 2
esac
