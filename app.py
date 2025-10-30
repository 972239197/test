import streamlit as st
import pandas as pd
import numpy as np
import ast
import json
from io import StringIO

# 页面配置
st.set_page_config(
    page_title="数组解析工具",
    page_icon="📊",
    layout="wide"
)

# 标题和描述

st.title("我的第一个 Streamlit 应用")
st.write("欢迎来到我的应用！")

name = st.text_input("请输入你的名字")
if name:
    st.success(f"你好，{name}!")
else:
    print("输入为空")  
st.markdown("""
这是一个强大的数组解析工具，支持多种格式的数组输入和解析。
支持格式：Python列表、NumPy数组、JSON数组、CSV数据等。
""")

# 1. 基础多选下拉菜单
st.header("1. 基础多选下拉菜单")

# 选项数据
fruits = ["苹果", "香蕉", "橙子", "草莓", "葡萄", "芒果", "西瓜"]
colors = ["红色", "蓝色", "绿色", "黄色", "紫色", "橙色", "粉色"]
programming_languages = ["Python", "JavaScript", "Java", "C++", "Go", "Rust", "TypeScript"]

# 多选下拉菜单
selected_fruits = st.multiselect(
    "选择你喜欢的水果:",
    fruits,
    default=["苹果", "香蕉"],
    help="可以选择多个水果"
)

st.write(f"**你选择的水果:** {selected_fruits}")

# 侧边栏
with st.sidebar:
    st.header("设置")
    array_type = st.selectbox(
        "选择数组类型",
        ["Python列表", "NumPy数组", "JSON数组", "CSV数据", "纯数字"]
    )
    
    st.markdown("---")
    st.markdown("### 使用说明")
    st.info("""
    1. 选择数组类型
    2. 输入或上传数组数据
    3. 点击解析按钮
    4. 查看解析结果和统计信息
    """)

# 主内容区域
tab1, tab2, tab3 = st.tabs(["📝 输入数据", "📤 上传文件", "❓ 示例"])

with tab1:
    st.subheader("手动输入数据")
    
    # 根据选择的数组类型显示不同的输入框
    if array_type == "Python列表":
        input_data = st.text_area(
            "输入Python列表",
            value="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
            height=100,
            help="例如: [1, 2, 3] 或 [[1,2], [3,4]]"
        )
    elif array_type == "JSON数组":
        input_data = st.text_area(
            "输入JSON数组",
            value='[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]',
            height=100,
            help="例如: [1, 2, 3] 或 [{\"key\": \"value\"}]"
        )
    elif array_type == "NumPy数组":
        input_data = st.text_area(
            "输入NumPy数组",
            value="np.array([1, 2, 3, 4, 5])",
            height=100,
            help="例如: np.array([1, 2, 3])"
        )
    elif array_type == "纯数字":
        input_data = st.text_area(
            "输入数字（用逗号、空格或换行分隔）",
            value="1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
            height=100,
            help="例如: 1 2 3 或 1,2,3 或 1\\n2\\n3"
        )
    else:  # CSV数据
        input_data = st.text_area(
            "输入CSV数据",
            value="name,age,score\nAlice,25,95\nBob,30,87\nCharlie,35,92",
            height=100,
            help="第一行通常是列名，后面是数据行"
        )
# 解析按钮
if st.button("🚀 解析数组", type="primary"):
    try:
        # 解析数据
        if array_data is None:
            if array_type == "Python列表":
                array_data = ast.literal_eval(input_data)
            elif array_type == "JSON数组":
                array_data = json.loads(input_data)
            elif array_type == "NumPy数组":
                # 提取数组部分
                if "np.array" in input_data:
                    array_str = input_data.split("np.array")[1].strip()
                    array_data = ast.literal_eval(array_str)
                else:
                    array_data = ast.literal_eval(input_data)
                array_data = np.array(array_data)
            elif array_type == "纯数字":
                # 处理多种分隔符
                cleaned_input = input_data.replace('\n', ',').replace(' ', ',')
                numbers = [x.strip() for x in cleaned_input.split(',') if x.strip()]
                array_data = [float(x) if '.' in x else int(x) for x in numbers]
            else:  # CSV数据
                from io import StringIO
                array_data = pd.read_csv(StringIO(input_data))
        
        # 显示解析结果
        st.success("✅ 解析成功！")

    except Exception as e:
            st.warning(f"无法生成统计信息: {e}")
