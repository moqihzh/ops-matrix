# nvm是nodejs的包管理器，使用nvm随意切换nodejs版本

## 安装nvm
```shell
git clone https://github.com/nvm-sh/nvm.git

chmod +x install.sh

./install.sh

# 新开一个shell终端输入
nvm -v
# 安装完成

=============================================================================
# 如果github不稳定，可以使用国内地址(https://gitcode.net/mirrors/nvm-sh/nvm.git),
# 但install.sh脚本仍然会去拉取github.com地址，修改install.sh
# sed -i 's/github.com/gitcode.net\/mirrors/g' install.sh
```

## nvm命令介绍
```shell
nvm 
- ls-remote
- install 
- use 

```
## nvm设置使用国内源
```shell
cat >> .bashrc << EOF
export NVM_NODEJS_ORG_MIRROR=https://cdn.npmmirror.com/binaries/node
EOF

# 以下源地址任选其一
# 淘宝源
export NVM_NODEJS_ORG_MIRROR=https://cdn.npmmirror.com/binaries/node

# 腾讯源
export NVM_NODEJS_ORG_MIRROR=https://mirrors.cloud.tencent.com/nodejs-release/

# 华为源
export NVM_NODEJS_ORG_MIRROR=https://mirrors.cloud.tencent.com/nodejs-release/
```

## 安装nodejs
```shell
nvm install v14.19.0

nvm use v14.19.0

node -v
```

