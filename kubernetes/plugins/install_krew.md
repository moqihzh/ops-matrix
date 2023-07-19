# 安装
# https://krew.sigs.k8s.io/docs/user-guide/setup/install/
# Linux安装krew

```shell
# 1. 安装git
CentOS: yum -y install git
Ubuntu: apt install git

# 2. 安装krew
cat > install_krew.sh < EOF
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
EOF

bash install_krew.sh

# 3. 加入环境变量
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
# 4. 运行
kubectl krew
```