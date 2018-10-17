# post文件接受服务器(dev)
### 默认端口 8000

##### 安装
```shell
pip install -r requirements.txt
python manage.py makemigrations file
python manage.py migrate
```

##### 运行

```shell
python .\manage.py runserver 0.0.0.0:8000
```