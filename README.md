<p align="center">
	<img alt="logo" src="https://foruda.gitee.com/avatar/1677189584093051772/9844924_dong-puen_1656601856.png!avatar200">
</p>
<h1 align="center" style="margin: 30px 0 30px; font-weight: bold;">Fir Easy v1.0.0</h1>
<h4 align="center">基于FastAPI实现SpringBoot结构的Python后端开发框架</h4>
<p align="center">
	<img src="https://img.shields.io/badge/Fir%20Easy-v1.0.0-da282a"></a>
	<img src="https://img.shields.io/github/license/mashape/apistatus.svg"></a>
</p>

## 项目简述

使用**FastAPI**。

```
https://fastapi.tiangolo.com/zh
```

FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 并基于标准的 Python 类型提示。

|       功能        | 实现 |
| :---------------: | :--: |
|  SpringBoot风格   |  ✔   |
| MySQL+TortoiseORM |  ✔   |
| 登录与令牌拦截器  |  ✔   |
|     配置文件      |  ✔   |
|  全局异常处理器   |  ✔   |
|    统一返回值     |  ✔   |
|    Swaager风格    |  ✔   |
### 项目结构

目录尽量符合Java编程风格

```
─src
  ├─api
  │  └─v1  
  ├─common
  ├─config
  │  ├─filter
  │  └─initialize
  ├─dependencies
  ├─dto
  ├─entity
  ├─logs
  ├─mapper
  │  └─impl
  ├─resources
  ├─servicepy
  │   └─impl
  └─application.py
```

### 为什么这样做？
ps:因为我是一个Java开发人员,朋友也都是Java开发人员,没想到现在AI趋势越来越大,我们需要使用python来实现一部分功能。
所以创建了该项目。但是我特意保留了一部分味道。

##  安装

推荐使用python=3.11

### 直接安装
```
pip install -r requirements.txt
```

### conda环境安装
```shell
conda create -n fastapi python=3.11
```

环境依赖安装

```shell
pip install -r requirements.txt
```

## 启动项目

### 编辑工具启动

支持**run**与**debug**

### 命令行

```
python application.py
```
添加启动参数, 切换环境
```shell
python application.py --active test
```

## 开发文档

详见 [开发文档](doc\doc.md) 
