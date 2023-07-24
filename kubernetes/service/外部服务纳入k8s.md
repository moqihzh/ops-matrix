apiVersion: v1
kind: Endpoints
metadata:
  name: jenkins
  namespace: default
subsets:
  - addresses:
      - ip: 192.168.0.123
    ports:
      - port: 8081
        protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: jenkins
  name: jenkins
  namespace: default
spec:
  ports:
    - port: 80
      protocol: TCP
      targetPort: 8080
  type: NodePort
