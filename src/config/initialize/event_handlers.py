import os

from fastapi import FastAPI
import socket
import logging

log = logging.getLogger("uvicorn")


def register_events(app: FastAPI):
    """
    服务启动与关闭触发方法
    :param app: FastAPI框架服务应用对象
    :return: pass
    """

    @app.on_event("startup")
    async def startup_event():
        """
        服务启动触发方法
        :return:
        """
        log.info("服务启动成功!")

        # 获取当前设备的主机名
        hostname = socket.gethostname()
        # 根据主机名获取本地网络的 IP 地址
        ip_address = socket.gethostbyname(hostname)

        server_port = os.environ.get('SERVER.PORT')
        server_port = int(server_port)
        http = "http"
        log.info(f"接口文档: {http}://{ip_address}:{server_port}/swagger-ui.html")
        log.info(f"服务地址: {http}://{ip_address}:{server_port}")

    @app.on_event("shutdown")
    async def shutdown_event():
        """
        服务关闭触发方法
        :return:
        """
        log.info("服务关闭!")
