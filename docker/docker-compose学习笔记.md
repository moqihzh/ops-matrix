## docker-compose 编写
```
version: "3"
services:
  nginxWebUi-server:
    image: cym1102/nginxwebui:latest
    volumes:
      - type: bind
        source: "/data/nginxwebui"
        target: "/home/nginxWebUI"
    environment:
      BOOT_OPTIONS: "--server.port=8080"
    ports:
    - "18080:8080"
```

## docker-compose 命令
```
# 后台进程启动项目
docker-compose up -d  

# 停止当前项目的所有服务，并移除网络
docker-compose  down

# 进入某个服务容器内部
docker-compose exec 服务id

# 列出项目中所有的容器
docker-compose ps

- -q # 显示容器id

# 启动docker-compose中的所有服务
docker-compose start 


# 停止docker-compose中的所有服务
docker-compose stop 

如果接上service_name，停止某个容器

# 重启所有服务
docker-compose restart 

如果接上service_name，重启某一个或多个容器

# 删除容器
docker-compose rm 

如果接上service_name，删除某个容器

- -f 强制删除容器
- -v 删除容器的数据卷，谨慎使用

# 查看项目内所有服务的进程
docker-compose top
如果接上service_name，只查看某个容器服务进程

# 暂停docker-compose的所有服务
docker-compose unpause



# 查看服务容器的日志
docker-compose logs

如果接上service_name，只查看某个容器服务的日志

- -f 实时打印日志
```