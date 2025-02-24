# Django教程
>
> <https://www.w3cschool.cn/django/django-first-app.html>

#### 创建Django项目

```bash
django-admin startproject projectname
```

#### 创建Django应用

```bash
python manage.py startapp appname
```

#### 执行数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 运行开发服务器

```bash
python manage.py runserver
```

#### 创建超级用户

```bash
python manage.py createsuperuser
```

#### 执行数据库 shell

```bash
python manage.py shell
```

#### 执行数据库管理命令

```bash
python manage.py dbshell
```

#### 执行测试命令

```bash
python manage.py test
```

#### 预览邮件内容

```bash
python manage.py sendtestemail
```

#### 显示Django版本信息

```bash
python -m django --version
```

#### 显示Django配置信息

```bash
python manage.py diffsettings
```

#### 清理构建文件

```bash
python manage.py clean
```

#### 优化数据库查询

```bash
python manage.py inspectdb
```

#### 重命名模型、字段或表

```bash
python manage.py rename
```

#### 生成静态文件

```bash
python manage.py collectstatic
```
