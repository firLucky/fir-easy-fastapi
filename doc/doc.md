# 开发文档

## 命名约定

在 Python 中，通常推荐使用 **小写字母和下划线**（snake_case）作为命名约定，而不是 Java 中常用的 **大驼峰命名**（CamelCase）。这是 Python 的 **PEP 8** 风格指南的推荐做法，它规定了 Python 代码的命名习惯。

### Python 常见的命名约定：

1. **类名**：使用大驼峰命名（CamelCase）。
   - 例如：`UserService`，`MySQLUserService`。
2. **函数名，方法名，文件名**：使用小写字母和下划线（snake_case）。
   - 例如：`create_user()`，`get_all_users()`，`user_department_dto.py`。
3. **变量名**：使用小写字母和下划线（snake_case）。
   - 例如：`user_service`，`user_id`。
4. **常量**：使用全大写字母和下划线（UPPERCASE_WITH_UNDERSCORES）。
   - 例如：`MAX_RETRIES`，`API_URL`。
## 环境安装

详见 [环境安装文档](environment.md) 

## 业务开发

详见 [开发业务接口](business_architecture.md) 

## FAQ

详见 [常见问题](faq.md) 
