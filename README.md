# cdbSPAAlbum

采用django rest framework

提供 登录 注册 上传 等 功能的 图站接口

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
            "imgurl": "[\"static/picture/img/1559436704395AC48A7A58AAA9FBA9DEA54CAF0EDE.jpg\", \"static/picture/img/1559436705593813C809182DCFAEC29F6B6CE93F17.jpg\", \"static/picture/img/15594367063106223BD87DD6781D4169591AEA9DEE.jpg\", \"static/picture/img/1559436707A53CFCE1BB7CC9865EEFAAE8C0D79827.jpg\", \"static/picture/img/1559436708B4F43F1028DE8102E0B870DB07F458B6.jpg\", \"static/picture/img/1559436709D52310CAA1924FD44D98894A150F0B22.jpg\", \"static/picture/img/1559436710D453DB5E044EF8CB712DD6824A21EC85.jpg\", \"static/picture/img/1559436711BAE822B605D096723D01BB260F451400.jpg\", \"static/picture/img/1559436712DAAC1C419B4046EF0FBB9EE806909020.jpg\"]",
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



### 修改配置

```python
#settings.py

#第28行 改成你的域名
ALLOWED_HOSTS = ["127.0.0.1","www.******.com",]

#第96行 改成你的mysql密码
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "HOST":"127.0.0.1",
        "PORT":3306,
        'NAME':"cdbSPAAlbumProject",
        "USER":"root",
        "PASSWORD":"********"
    }
}
```



### 创建数据库

```sql
CREATE DATABASE cdbSPAAlbumProject DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
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



##### 联系方式

 最近一直被恶意举报加不了qq可以b站私信我，

