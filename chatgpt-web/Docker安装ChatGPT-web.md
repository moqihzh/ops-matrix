# 安装ChatGPT-Web

## 下载chatgpt-web项目
```
git clone https://github.com/Chanzhaoyu/chatgpt-web.git
```
## 安装Docker
```
git clone https://github.com/x-hanzh/ops-matrix.git

cp -a ops-matrix/repo/CentOS/docker-ce.repo /etc/yum.repo.d/

yum -y install docker-ce

systemctl start docker 

systemctl enable docker
```

## 安装docker-compose
```
pip3 install docker-compose
```

## 安装node,pnpm
### 安装Node16版本
```
git clone https://github.com/nvm-sh/nvm.git

bash nvm/install.sh

# 重新打开终端，键入
nvm -v

# 安装npm
nvm install 16.19.0
nvm use 16.19.0

# 验证npm和node是否安装完成
node -v

npm -v

```
### pnpm
```
npm install pnpm -g
```
## 构建编译chatgpt前端
```
cd chatgpt-web

pnpm install 

pnpm build

cp -a dist/* docker-compose/nginx/html/
```

## 修改配置
```
cd docker-compose

cat docker-compose.yml

# 修改api-key 
OPENAI_API_KEY: xxxxxxxxxxx
# 修改模型配置，默认gpt-3.5-turbo，可选
OPENAI_API_MODEL: gpt-3.5-turbo
```

## 启动项目
```
docker-compose up -d 
```

## 访问chatgpt-web
http://IP:3002