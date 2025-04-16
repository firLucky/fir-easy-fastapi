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

## 

### 流式接口

详见接口**/ai/chat**

```python
@ai_router.post(
    "/chat",
    summary="流式对话",
    description="接受用户问题，进行流式回答",
    response_description="对话返回数据",
    response_model=StateDTOResponse,
)
async def ai_chat(
        ai_chat_body_dto: AiChatBodyDTO = Body(description="更新用户"),
        ai_service: AiService = Depends(get_ai_service)):
    data = await ai_service.ai_chat(ai_chat_body_dto)
    return data
```

### python代码测试

可使用以下方法进行测试

```python
import requests


def stream_post_request(url, token, data=None, json=None):
    """
    流式调用 POST 接口

    :param url: 接口地址
    :param token: 认证令牌
    :param data: 要发送的表单数据
    :param json: 要发送的 JSON 数据
    """

    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json'
    }
    # 使用 stream=True 参数启用流式传输
    with requests.post(url, headers=headers, json=json, data=data, stream=True) as response:
        # 检查响应状态码
        if response.status_code != 200:
            raise Exception(f"请求失败，状态码: {response.status_code}")

        # 逐行处理响应内容
        for line in response.iter_lines():
            if line:  # 过滤掉保持连接的空行
                decoded_line = line.decode('utf-8')
                print(decoded_line)

# 使用示例
api_url = "http://127.0.0.1:8080/ai/chat"
api_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQ4NTE5MzUsInVpZCI6IjEiLCJ1bmFtZSI6ImZpciJ9.0MjiM6xmCKMqbrdNUA8mKXP85Mj8bRQnculx1lygMzc"
payload = {
    "msg": "你是谁",
    "stream": True
}

stream_post_request(api_url, api_token, json=payload)
```

将会逐行获取到数据

```
{"content": "你好，"}
{"content": "我是"}
{"content": "Chat"}
{"content": "我可以"}
{"content": "帮助你"}
{"content": "解答各"}
{"content": "种问题，"}
{"content": "包括"}
{"content": "编程、"}
{"content": "写作、"}
{"content": "学习等。"}
{"content": "如果你"}
{"content": "有任何问题，"}
{"content": "请随时告诉我！"}
{"content": "我会尽力"}
{"content": "提供最"}
{"content": "准确的"}
{"content": "答案。"}
{"content": "现在"}
{"content": "就开"}
{"content": "始交"}
{"content": "流吧！"}
```

### 前端请求

对于前端可以采用**fetch**流式传输请求，示例如下

```typescript

/**
 * fetch流式传输
 * 适配后端media_type="text/plain"形式的流式传输
 *
 * @param method 请求类型
 * @param url 请求地址
 * @param data 请求数据
 */
export async function streamApi(method: string, url: string, data: any): Promise<Response> {
  const token = localStorage.getItem('at')
  url = masterService + url
  const response = await fetch(url, {
    method: method,
    headers: {
      'Authorization': `${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  if (response.ok) {
    // pass
  }
  return response
}
```

```typescript
import { streamApi } from '@/utils/request/request.ts'

export default {
  ai: {
    painterChat: (data?: any): Promise<Response> => streamApi('post', '/ai/painter/test', data)
  }
}
```

```typescript
  try {
    const data = {
      content: userMassage
    }
    const response = await api.ai.painterChat(data)
    if (!response.ok) {
      return
    }
    // 获取可读流
    if (!response.body) {
      return
    }
    // 新增检查
    const reader = response.body.getReader()
    const decoder = new TextDecoder('utf-8')
    let buffer = ''

    while (true) {
      const { done, value } = await reader.read()
      if (done) break // 流结束
      // 解码当前块并添加到缓冲区
      buffer += decoder.decode(value, { stream: true })

      if (buffer) {
        // 处理缓冲区中的数据（假设后端按 \n 分割）
        const lines = buffer.split('\n')
        if (!response.body) {
          return
        } // 新增检查
        buffer = lines.pop() || '' // 剩余部分保留到下一次处理
        if(buffer == null || buffer != ""){
          const jsonObject = JSON.parse(buffer)
          if (jsonObject.code === 401){
            ElMessage.error(`登录失败`)
            localStorage.removeItem('at')
            // 跳转到主页
            router.push({
              path: '/login'
            }).catch(error => {
              console.error(error)
            })
          }else {

          }
        }
        for (const line of lines) {
          if (line.trim()) {
            try {
              const jsonObject = JSON.parse(line)
              content.value = content.value + jsonObject.content
            } catch (e) {
              // pass
            }
          }
        }
      }
    }
  } catch (error) {
    // pass
  }
```

## FAQ

详见 [常见问题](faq.md) 
