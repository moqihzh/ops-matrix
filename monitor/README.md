# 源地址：https://github.com/starsliao/Prometheus
# kube-state-metrics部署在monitoring命名空间
```shell
kubectl create namespace monitoring
kubectl apply -f kube-state-metrics.yaml
```
# 修改Prometheus配置文件
## cadvisor的job下增加以下内容：
```prometheus
    metric_relabel_configs:
    - source_labels: [instance]
      separator: ;
      regex: (.+)
      target_label: node
      replacement: $1
      action: replace
```
## 添加job_name
```prometheus
  - job_name: kube-state-metrics
    honor_timestamps: false
    scrape_interval: 30s
    scrape_timeout: 10s
    metrics_path: /metrics
    scheme: http
    static_configs:
    - targets:
      - kube-state-metrics.monitoring.svc.local:8080

# 重载prometheus配置
curl -XPOST http://prometheus-server.monitoring/-/reload
```