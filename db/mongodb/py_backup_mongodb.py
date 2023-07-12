import subprocess
import datetime

# MongoDB连接信息
mongo_host = '127.0.0.1'
mongo_port = 27017
mongo_db = ''
mongo_user=''
mongo_password=''

# 备份目录
backup_dir = './'

# 获取当前日期时间
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d')

# 构建备份文件路径
backup_file = backup_dir + '_' + current_datetime

# 构建mongodump命令
mongodump_cmd = f'mongodump --host {mongo_host} --username {mongo_user} --password {mongo_password}  --port {mongo_port} --authenticationDatabase admin  -d {mongo_db} -o {backup_file}'

# 执行mongodump命令
subprocess.run(mongodump_cmd, shell=True)
