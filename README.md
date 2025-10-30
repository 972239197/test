# test
https://share.streamlit.io/
部署前准备
1. 创建 Streamlit 应用
首先确保你有一个有效的 Streamlit 应用文件（通常命名为 app.py）：

python
import streamlit as st

st.title("我的第一个 Streamlit 应用")
st.write("欢迎来到我的应用！")

name = st.text_input("请输入你的名字")
if name:
    st.success(f"你好，{name}！")
2. 创建 requirements.txt 文件
列出你的应用所需的所有依赖包：

text
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.21.0
部署步骤
方法一：通过 Streamlit Community Cloud 直接部署
访问社区云

前往 share.streamlit.io

使用 GitHub 账号登录

连接 GitHub 仓库

点击 "New app"

选择你的 GitHub 仓库

选择分支（通常是 main 或 master）

指定主文件路径（如 app.py）

部署配置

Streamlit Community Cloud 会自动检测配置

点击 "Deploy" 开始部署

方法二：通过命令行部署
安装 Streamlit（如果尚未安装）

bash
pip install streamlit
在项目根目录创建配置文件
创建 .streamlit/config.toml：

toml
[server]
headless = true
项目结构示例
确保你的项目有正确的结构：

text
my-streamlit-app/
├── app.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
└── README.md
高级配置
1. 自定义主题
在 .streamlit/config.toml 中添加：

toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
2. 环境变量配置
在 Streamlit Community Cloud 的部署界面中：

进入应用设置

添加环境变量

如 API keys、数据库连接等

常见问题解决
部署失败的可能原因：
依赖问题：检查 requirements.txt 格式是否正确

文件路径错误：确保主文件路径正确

内存不足：优化应用内存使用

端口冲突：确保使用默认端口

查看日志：
在 Streamlit Community Cloud 控制台查看部署日志

排查错误信息