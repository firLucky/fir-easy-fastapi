# 环境安装

### conda环境安装

下载anaconda用于管理python虚拟环境

```
https://www.anaconda.com/download/success
```

安装完后，使用一下命令创建虚拟环境

```shell
conda create -n fir-easy-fastapi python=3.11
```

安装完之后，切换环境

```
conda activate fir-easy-fastapi
```

## 导出当前环境

```
pip list --format=freeze >requirements.txt
```



环境依赖安装

```shell
pip install -r requirements.txt
```

删除环境

先切换到基础环境

```
conda activate base
```

使用一下命令删除，遇见选择填写y

```
conda remove -n fir-easy-fastapi --all
```
