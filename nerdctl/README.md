# 安装nerdctl
```shell
VERSION="v1.5.0"
TARGET_PATH="/usr/local/bin/"

# wget -c https://github.com/containerd/nerdctl/releases/download/${VERSION}/nerdctl-${VERSION}-linux-amd64.tar.gz

# tar zxvf buildkit-v0.12.1.linux-amd64.tar.gz -C $TARGET_PATH

```
# 验证
```shell
# nerdctl --version
nerdctl version 1.5.0
```

> 构建容器镜像需安装buildkit工具


# 安装buildkit
```shell
VERSION="v0.12.1"
TARGET_PATH="/usr/local/bin/"

# wget -c https://github.com/moby/buildkit/releases/download/${VERSION}/buildkit-${VERSION}.linux-amd64.tar.gz

# tar zxvf buildkit-v0.12.1.linux-amd64.tar.gz -C $TARGET_PATH

# cat >> buildkit.socket << EOF
[Unit]
Description=BuildKit
Documentation=https://github.com/moby/buildkit

[Socket]
ListenStream=%t/buildkit/buildkitd.sock
SocketMode=0660

[Install]
WantedBy=sockets.target
EOF

# cat >>  buildkit.service << EOF 
[Unit]
Description=BuildKit
Requires=buildkit.socket
After=buildkit.socket
Documentation=https://github.com/moby/buildkit

[Service]
Type=notify
ExecStart=/usr/local/bin/buildkitd --addr fd://

[Install]
WantedBy=multi-user.target
EOF


# systemctl enable buildkit.service
Created symlink from /etc/systemd/system/multi-user.target.wants/buildkit.service to /usr/lib/systemd/system/buildkit.service.

# systemctl start buildkit.service
# systemctl status buildkit.service
# systemctl enable buildkit.service
Created symlink from /etc/systemd/system/multi-user.target.wants/buildkit.service to /usr/lib/systemd/system/buildkit.service.
[root@ecs-344692 data]# systemctl status buildkit.service
● buildkit.service - BuildKit
   Loaded: loaded (/usr/lib/systemd/system/buildkit.service; enabled; vendor preset: disabled)
   Active: active (running) since Sun 2023-08-13 08:59:52 CST; 50min ago
     Docs: https://github.com/moby/buildkit
 Main PID: 12614 (buildkitd)
   CGroup: /system.slice/buildkit.service
           └─12614 /usr/local/bin/buildkitd --addr fd://

Aug 13 08:59:52 ecs-344692 buildkitd[12614]: time="2023-08-13T08:59:52+08:00" level=info msg="found worker \"rixmyuwcxqpelw8r5iv0iwkf...cutor:c
Aug 13 08:59:52 ecs-344692 buildkitd[12614]: time="2023-08-13T08:59:52+08:00" level=info msg="found 2 workers, default=\"j7smp7wfbuwf...0fap\""
Aug 13 08:59:52 ecs-344692 buildkitd[12614]: time="2023-08-13T08:59:52+08:00" level=warning msg="currently, only the default worker c... used."
Aug 13 08:59:52 ecs-344692 buildkitd[12614]: time="2023-08-13T08:59:52+08:00" level=info msg="running server on /run/buildkit/buildkitd.sock"
Aug 13 08:59:52 ecs-344692 systemd[1]: Started BuildKit.
Aug 13 09:00:22 ecs-344692 buildkitd[12614]: time="2023-08-13T09:00:22+08:00" level=error msg="/moby.buildkit.v1.Control/Solve return... found"
Aug 13 09:01:41 ecs-344692 buildkitd[12614]: time="2023-08-13T09:01:41+08:00" level=error msg="/moby.buildkit.v1.Control/Solve return...nceled"
Aug 13 09:03:29 ecs-344692 buildkitd[12614]: time="2023-08-13T09:03:29+08:00" level=info msg="trying next host" error="pull access de...09d23c0
Aug 13 09:03:29 ecs-344692 buildkitd[12614]: time="2023-08-13T09:03:29+08:00" level=error msg="/moby.buildkit.v1.frontend.LLBBridge/S...failed"
Aug 13 09:03:29 ecs-344692 buildkitd[12614]: time="2023-08-13T09:03:29+08:00" level=error msg="/moby.buildkit.v1.Control/Solve return...failed"
Hint: Some lines were ellipsized, use -l to show in full.

```

# 验证
```shell
# buildkitd --version
buildkitd github.com/moby/buildkit v0.12.1 bb857a0d49f45aa0ce9cd554b78d4075553e20f9
```