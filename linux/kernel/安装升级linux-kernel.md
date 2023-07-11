# CentOS
## YUM升级内核
```
yum -y update
```

## 安装repo
```
git clone https://github.com/x-hanzh/ops-matrix.git

cd ops-matrix/repo/CentOS/kernel.repo

cp -a kernel.repo /etc/yum.repos.d
```

## 查看内核包
```
yum --disablerepo="*" --enablerepo="elrepo-kernel" list available
```

## 安装kernel
```
# 最新版
yum --enablerepo=elrepo-kernel install kernel-ml

# 长期支持版
yum --enablerepo=elrepo-kernel install kernel-lt
```

## 修改内核默认启动项
```
sed -i 's/GRUB_DEFAULT=saved/GRUB_DEFAULT=0/g' /etc/default/grub

grub2-mkconfig -o /boot/grub2/grub.cfg
```

## 重启并查看内核版本
```
reboot 

uname -r 

```