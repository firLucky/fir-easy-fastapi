import argparse
import os

import uvicorn
from dotenv import load_dotenv
from src.api.server_app import fir_app
from src.config.initialize.initialize_utils import initialize_trigger
from src.config.initialize.launch_title import start


def main():
    """
    项目启动方法
    """
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="Example script to demonstrate command line arguments.")
    # 添加参数
    parser.add_argument('--active', type=str)
    # 解析命令行参数
    args = parser.parse_args()

    start()
    # 执行项目启动前的初始化
    initialize_trigger()
    env_active = args.active
    if env_active is None:
        env_active = "dev"
    env_file = f'src/resources/{env_active}.env'

    if os.path.exists(env_file):
        load_dotenv(env_file)
        server_port = os.environ.get('SERVER_PORT')
        server_port = int(server_port)
        uvicorn.run(fir_app, host="0.0.0.0", port=server_port, log_config="src/resources/uvicorn_config.json",
                    use_colors=True,
                    loop="asyncio",
                    )
    else:
        raise Exception(".启动失败--env配置文件不存在")


if __name__ == "__main__":
    # 启动主程序方法
    main()
