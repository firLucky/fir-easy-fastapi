# FAQ

##  以一种访问权限不允许的方式做了一个访问套接字的尝试

报错如下，表示端口被占用

```
vicorn main:app --reload
INFO:     Will watch for changes in these directories: 
ERROR:    [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。
```

## ERROR: To modify pip, please run the following command:

需要 **升级 pip 工具到最新版本**，升级命令如下

```
 python -m pip install --upgrade pip
```

