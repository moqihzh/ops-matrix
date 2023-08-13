# 安装
## 网络安装
```shell
yum -y install nginx
```

# 本地安装rpm
> rpm包必须包含依赖包，否则安装失败
```shell
yum -y localinstall *.rpm
```

# 安装开发工具套件
```
yum -y groupinstall 'Development Tools'
```

# 卸载软件
```shell
yum -y remove nginx
```