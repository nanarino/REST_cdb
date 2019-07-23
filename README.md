# REST_cdb

采用django rest framework

为前端项目：SPA_cdb,提供api接口

未完成 目前只完成了认证和图片的接口

项目和人 都有待改进

接口示例：

```python
GET /api/albums/?page=1&size=1

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
{
    "count": 4,
    "next": "http://www.******.com/api/albums/?page=2&size=1",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "时雨最可爱",
            "imglen": "9",
            "motif": "舰C",
            "time": "2019-06-02T08:51:44.769952+08:00",
            "publisher": {
                "id": 1,
                "username": "kogawananari"
            }
        }
    ]
}
```



### 环境

```python
python3.7
MySQL5.7
```



### 安装依赖

```cmd
cd cdbspaAlbum

pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

​    django版本： 1.11.20



### 修改配置

```python
#settings.py

#第28行 改成你的域名
ALLOWED_HOSTS = ["127.0.0.1","www.******.com",]

#第88行 改成你的mysql密码
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "HOST":"127.0.0.1",
        "PORT":3306,
        'NAME':"REST_cdb",
        "USER":"root",
        "PASSWORD":"********"
    }
}
```



### 创建数据库

```sql
CREATE DATABASE REST_cdb DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```



### 迁移数据库

```cmd
python3 manage.py makemigrations   

python3 manage.py migrate   
```



### 生成超级管理员

```cmd
python3 manage.py createsuperuser
```



### 启动服务

```cmd
python3 manage.py runserver 0.0.0.0:80
```


