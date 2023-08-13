#!/usr/bin/env bash
# author: liy
# file: containerd_mirrors.sh
#
 
export PS4='\[\e[35m\]+ $(basename $0):${FUNCNAME}:$LINENO: \[\e[0m\]'
[ "$debug" == "true" -o "$debug" == "yes" ] && set -x
 
config_file="/etc/containerd/config.toml"
config_path='/etc/containerd/certs.d'
 
if [ ! -f "${config_file}" ];then
    [ ! -d "${config_file%/*}" ] && mkdir -p ${config_file%/*}
    lineno="$(containerd config default | grep -n -A 1 -P '(?<=\[plugins.")io.containerd.grpc.v1.cri(?=".registry])'|tail -1)"
    lineno=${lineno/-*}
    containerd config default | sed -e "${lineno}s@config.*@config_path = \"${config_path}\"@" |sed '/SystemdCgroup/s/false/true/' > $config_file
fi
 
[ ! -d "${config_path}" ] && mkdir -p ${config_path}
params="${@:-registry.k8s.io:k8s.m.daocloud.io docker.io:docker.m.daocloud.io gcr.io:gcr.m.daocloud.io k8s.gcr.io:k8s.m.daocloud.io quay.io:quay.m.daocloud.io}"
 
function content(){
    printf 'server = "https://%s"\n'  "${registry}"
    printf '[host."https://%s"]\n' "${proxy_server}"
    printf '  capabilities = ["pull", "resolve"]'
}
 
for param in ${params}
do
    registry="${param/:*/}"
    proxy_server="${param/*:/}"
    hosts_path="$config_path/$registry"
    [ ! -d "$hosts_path" ] && mkdir -p ${hosts_path}
    content > $hosts_path/hosts.toml
done
