from kubernetes import client, config

# 或者使用 config.load_incluster_config() 链接 Python 到 Kubernetes 集群
config.load_kube_config()  

# Kubernetes API 客户端
v1 = client.AppsV1Api()  


# 查询默认命名空间中的所有 Deployment
deployments = v1.list_namespaced_deployment(namespace="default")  

# 修改 Deployment 的 revisionHistoryLimit
for deployment in deployments.items:
    deployment.spec.revision_history_limit = 3  
    v1.patch_namespaced_deployment(name=deployment.metadata.name, namespace=deployment.metadata.namespace, body=deployment)
    print(deployment.metadata.name + '\t' + "patch success")

print('update successful')
