import subprocess
import datetime

# PostgreSQL连接信息
pg_host = '127.0.0.1'
pg_port = 5432 
pg_user = 'root'
pg_password = ''
pg_db = 'postgres'

# 备份目录
backup_dir = './'

# 获取当前日期时间
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# 构建备份文件路径
backup_file =  backup_dir + pg_db + '_' + current_datetime + '.sql'

# 构建pg_dump命令
pg_dump_cmd = f'export PGPASSWORD={pg_password} && pg_dump --host={pg_host} --port={pg_port} --username={pg_user} --dbname={pg_db} --file={backup_file}'

# 执行pg_dump命令
subprocess.run(pg_dump_cmd, shell=True)

