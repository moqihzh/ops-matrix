# 安装dotnet-sdk3.1
```shell

yum -y install dotnet-sdk-3.1

# 查看dotnet版本信息
dotnet info
```

# 安装kernel
```shell

# 安装长期支持版本
yum --enablerepo=elrepo-kernel install kernel-lt

或者

# 安装最新版
yum --enablerepo=elrepo-kernel install kernel-ml

# 设置grub2,并生成grub配置文件
grub2-set-default 0
grub2-mkconfig -o /boot/grub2/grub.cfg

# 重启系统
reboot

# 查看内核版本
uname -r 
```

# 安装openresty
```shell

# 安装openresty
yum -y install openresty

# 开机自启
systemctl enable openresty

# 启动openresty
systemctl start openresty
```

# 安装nginx
```shell

# 安装nginx
yum -y install nginx

# 开机自启
systemctl enable nginx

# 启动nginx
systemctl start nginx
```

# 安装mongodb
```shell

yum -y install mongodb-org

# 开机自启
systemctl enable mongod

# 启动mongodb
systemctl start mongod
```

# 安装docker-ce
```shell

yum -y install docker-ce

# 开机自启
systemctl enable docker

# 启动docker
systemctl start docker

# 查看docker版本
docker version
```