# kong
## docker-compose部署kong
### 启动
```
docker-compose up -d
```

### 停止
```
docker-compose stop
```

## 销毁
```
docker-compose down
```

## 重启
```
docker-compose restart
```

## 查看日志
```
# 查看docker-compose所有容器日志
docker logs -f --tail 10

# 查看某个容器日志
docker logs -f  --tail 10 <container_id>
```