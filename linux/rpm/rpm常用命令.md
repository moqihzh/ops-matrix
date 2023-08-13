# 安装/升级
```shell
rpm -ivh xxxx.rpm
```

# 卸载
```shell
rpm -e --nodeps xxx.rpm
```

# 批量卸载
```
rpm -qa|grep xxx.rpm|xargs -I {} rpm -e --nodeps  
```