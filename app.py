import streamlit as st
import pandas as pd
import numpy as np
import struct
import binascii
import re
from typing import Dict, List, Any
import matplotlib.pyplot as plt
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

st.markdown("""
这是一个强大的数组解析工具
""")

# 1. 基础多选下拉菜单
st.header("请选择设备类型")

# 选项数据
dev_type = ["Xmini", "X1.3重构", "X1.5", "Xmicrowave"]

# 多选下拉菜单
selected_dev = st.multiselect(
    "选择你要解析的设备",
    dev_type,
    default=["Xmini"],
)

st.write(f"**你选择的设备:** {selected_dev}")



# 页面配置
st.set_page_config(
    page_title="十六进制数据解析器",
    page_icon="🔢",
    layout="wide"
)

# 标题和描述
st.title("🔢 十六进制数据解析器")
st.markdown("""
这是一个专业的十六进制数据解析工具，支持多种数据格式的解析和转换。
支持：整数、浮点数、字符串、字节数组、协议解析等。
""")

# 会话状态初始化
if 'parsed_results' not in st.session_state:
    st.session_state.parsed_results = []

class HexParser:
    """十六进制数据解析器"""
    
    @staticmethod
    def clean_hex_string(hex_string: str) -> str:
        """清理十六进制字符串"""
        # 移除空格、换行、0x前缀等
        cleaned = re.sub(r'[^0-9A-Fa-f]', '', hex_string)
        return cleaned.upper()
    
    @staticmethod
    def hex_to_bytes(hex_string: str) -> bytes:
        """十六进制字符串转字节"""
        cleaned = HexParser.clean_hex_string(hex_string)
        if len(cleaned) % 2 != 0:
            raise ValueError("十六进制字符串长度必须为偶数")
        return bytes.fromhex(cleaned)
    
    @staticmethod
    def parse_integers(hex_data: str) -> Dict[str, Any]:
        """解析整数类型"""
        try:
            bytes_data = HexParser.hex_to_bytes(hex_data)
            results = {}
            
            # 8位整数
            if len(bytes_data) >= 1:
                results["8位无符号整数"] = struct.unpack('B', bytes_data[:1])[0]
                results["8位有符号整数"] = struct.unpack('b', bytes_data[:1])[0]
            
            # 16位整数 (小端序和大端序)
            if len(bytes_data) >= 2:
                results["16位无符号整数(大端)"] = struct.unpack('>H', bytes_data[:2])[0]
                results["16位有符号整数(大端)"] = struct.unpack('>h', bytes_data[:2])[0]
                results["16位无符号整数(小端)"] = struct.unpack('<H', bytes_data[:2])[0]
                results["16位有符号整数(小端)"] = struct.unpack('<h', bytes_data[:2])[0]
            
            # 32位整数
            if len(bytes_data) >= 4:
                results["32位无符号整数(大端)"] = struct.unpack('>I', bytes_data[:4])[0]
                results["32位有符号整数(大端)"] = struct.unpack('>i', bytes_data[:4])[0]
                results["32位无符号整数(小端)"] = struct.unpack('<I', bytes_data[:4])[0]
                results["32位有符号整数(小端)"] = struct.unpack('<i', bytes_data[:4])[0]
            
            # 64位整数
            if len(bytes_data) >= 8:
                results["64位无符号整数(大端)"] = struct.unpack('>Q', bytes_data[:8])[0]
                results["64位有符号整数(大端)"] = struct.unpack('>q', bytes_data[:8])[0]
                results["64位无符号整数(小端)"] = struct.unpack('<Q', bytes_data[:8])[0]
                results["64位有符号整数(小端)"] = struct.unpack('<q', bytes_data[:8])[0]
            
            return results
        except Exception as e:
            return {"错误": f"整数解析失败: {str(e)}"}
    
    @staticmethod
    def parse_floats(hex_data: str) -> Dict[str, Any]:
        """解析浮点数类型"""
        try:
            bytes_data = HexParser.hex_to_bytes(hex_data)
            results = {}
            
            # 32位浮点数
            if len(bytes_data) >= 4:
                results["32位浮点数(大端)"] = struct.unpack('>f', bytes_data[:4])[0]
                results["32位浮点数(小端)"] = struct.unpack('<f', bytes_data[:4])[0]
            
            # 64位浮点数
            if len(bytes_data) >= 8:
                results["64位浮点数(大端)"] = struct.unpack('>d', bytes_data[:8])[0]
                results["64位浮点数(小端)"] = struct.unpack('<d', bytes_data[:8])[0]
            
            return results
        except Exception as e:
            return {"错误": f"浮点数解析失败: {str(e)}"}
    
    @staticmethod
    def parse_strings(hex_data: str) -> Dict[str, Any]:
        """解析字符串类型"""
        try:
            bytes_data = HexParser.hex_to_bytes(hex_data)
            results = {}
            
            # ASCII 字符串
            ascii_str = ""
            for byte in bytes_data:
                if 32 <= byte <= 126:  # 可打印ASCII字符
                    ascii_str += chr(byte)
                else:
                    ascii_str += f"\\x{byte:02x}"
            results["ASCII字符串"] = ascii_str
            
            # UTF-8 字符串
            try:
                results["UTF-8字符串"] = bytes_data.decode('utf-8')
            except:
                results["UTF-8字符串"] = "非有效UTF-8编码"
            
            # Latin-1 字符串
            try:
                results["Latin-1字符串"] = bytes_data.decode('latin-1')
            except:
                results["Latin-1字符串"] = "解码错误"
            
            return results
        except Exception as e:
            return {"错误": f"字符串解析失败: {str(e)}"}
    
    @staticmethod
    def parse_basic_info(hex_data: str) -> Dict[str, Any]:
        """解析基本信息"""
        try:
            bytes_data = HexParser.hex_to_bytes(hex_data)
            cleaned_hex = HexParser.clean_hex_string(hex_data)
            
            return {
                "原始十六进制": hex_data,
                "清理后十六进制": cleaned_hex,
                "字节长度": len(bytes_data),
                "位长度": len(bytes_data) * 8,
                "字节数组": list(bytes_data),
                "二进制表示": ' '.join(format(byte, '08b') for byte in bytes_data)
            }
        except Exception as e:
            return {"错误": f"基本信息解析失败: {str(e)}"}
    
    @staticmethod
    def parse_protocol_specific(hex_data: str) -> Dict[str, Any]:
        """解析协议特定格式"""
        try:
            bytes_data = HexParser.hex_to_bytes(hex_data)
            results = {}
            
            # 简单的协议字段解析示例
            if len(bytes_data) >= 4:
                # 假设前4字节是头部
                results["协议头部"] = hex_data[:8]
                
            # MAC地址格式 (6字节)
            if len(bytes_data) == 6:
                mac = ':'.join(f'{b:02x}' for b in bytes_data)
                results["MAC地址"] = mac.upper()
            
            # IPv4地址格式 (4字节)
            if len(bytes_data) == 4:
                ip = '.'.join(str(b) for b in bytes_data)
                results["IPv4地址"] = ip
            
            # 颜色值解析
            if len(bytes_data) == 3:
                results["RGB颜色"] = f"RGB({bytes_data[0]}, {bytes_data[1]}, {bytes_data[2]})"
            elif len(bytes_data) == 4:
                results["ARGB颜色"] = f"ARGB({bytes_data[0]}, {bytes_data[1]}, {bytes_data[2]}, {bytes_data[3]})"
            
            return results
        except Exception as e:
            return {"错误": f"协议解析失败: {str(e)}"}

# 侧边栏配置
with st.sidebar:
    st.header("⚙️ 解析配置")
    
    parse_options = st.multiselect(
        "选择解析类型",
        ["基本信息", "整数类型", "浮点数类型", "字符串类型", "协议特定"],
        default=["基本信息", "整数类型"]
    )
    
    st.markdown("---")
    st.header("📊 示例数据")
    
    example_data = st.selectbox(
        "选择示例数据",
        ["自定义", "整数示例", "浮点数示例", "字符串示例", "MAC地址", "IP地址", "颜色值"]
    )
    
    st.markdown("---")
    st.header("❓ 使用说明")
    st.info("""
    1. 输入十六进制数据
    2. 选择解析类型
    3. 查看解析结果
    4. 可上传文件批量解析
    """)

# 主界面
st.header("📥 输入十六进制数据")

# 示例数据映射
example_map = {
    "整数示例": "DEADBEEF",
    "浮点数示例": "40490FDB",
    "字符串示例": "48656C6C6F20576F726C64",
    "MAC地址": "A1B2C3D4E5F6",
    "IP地址": "C0A80101",
    "颜色值": "FF8040"
}

# 数据输入区域
col1, col2 = st.columns([3, 1])

with col1:
    if example_data == "自定义":
        hex_input = st.text_area(
            "输入十六进制数据",
            height=100,
            placeholder="例如: 48656C6C6F20576F726C64 或 48 65 6C 6C 6F",
            help="支持带空格或不带空格的十六进制格式"
        )
    else:
        default_hex = example_map.get(example_data, "")
        hex_input = st.text_area(
            "输入十六进制数据",
            value=default_hex,
            height=100
        )

with col2:
    st.subheader("快速操作")
    if st.button("🔄 清理格式", use_container_width=True):
        if hex_input:
            cleaned = HexParser.clean_hex_string(hex_input)
            hex_input = cleaned
            st.rerun()
    
    if st.button("📋 复制示例", use_container_width=True):
        hex_input = "48656C6C6F20576F726C64"  # Hello World
    
    st.markdown("---")
    st.subheader("文件上传")
    uploaded_file = st.file_uploader(
        "上传十六进制文件",
        type=['txt', 'hex', 'bin'],
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        file_content = uploaded_file.getvalue().decode('utf-8')
        hex_input = file_content

# 解析按钮
if st.button("🚀 开始解析", type="primary", use_container_width=True):
    if hex_input:
        try:
            # 执行解析
            results = {
                "timestamp": pd.Timestamp.now(),
                "original_input": hex_input
            }
            
            # 根据选择的选项进行解析
            if "基本信息" in parse_options:
                results["basic_info"] = HexParser.parse_basic_info(hex_input)
            
            if "整数类型" in parse_options:
                results["integers"] = HexParser.parse_integers(hex_input)
            
            if "浮点数类型" in parse_options:
                results["floats"] = HexParser.parse_floats(hex_input)
            
            if "字符串类型" in parse_options:
                results["strings"] = HexParser.parse_strings(hex_input)
            
            if "协议特定" in parse_options:
                results["protocol"] = HexParser.parse_protocol_specific(hex_input)
            
            st.session_state.parsed_results.append(results)
            st.success("✅ 解析完成！")
            
        except Exception as e:
            st.error(f"❌ 解析失败: {str(e)}")
    else:
        st.warning("⚠️ 请输入十六进制数据")

# 显示解析结果
if st.session_state.parsed_results:
    latest_result = st.session_state.parsed_results[-1]
    
    st.header("📊 解析结果")
    
    # 创建标签页显示不同方面的结果
    tabs = st.tabs(["🔍 综合视图", "📈 数据可视化", "📋 解析详情", "💾 导出数据"])
    
    with tabs[0]:
        st.subheader("综合解析结果")
        
        # 基本信息卡片
        if "basic_info" in latest_result and "错误" not in latest_result["basic_info"]:
            basic_info = latest_result["basic_info"]
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("字节长度", basic_info.get("字节长度", 0))
            with col2:
                st.metric("位长度", basic_info.get("位长度", 0))
            with col3:
                st.metric("十六进制字符", len(basic_info.get("清理后十六进制", "")))
            with col4:
                st.metric("解析时间", latest_result["timestamp"].strftime("%H:%M:%S"))
        
        # 快速查看重要结果
        st.subheader("关键解析结果")
        
        cols = st.columns(2)
        
        with cols[0]:
            if "integers" in latest_result:
                integers = latest_result["integers"]
                if "错误" not in integers:
                    st.write("**整数解析:**")
                    for key, value in list(integers.items())[:4]:  # 显示前4个
                        st.code(f"{key}: {value}")
        
        with cols[1]:
            if "strings" in latest_result:
                strings = latest_result["strings"]
                if "错误" not in strings:
                    st.write("**字符串解析:**")
                    st.code(f"ASCII: {strings.get('ASCII字符串', '')}")
    
    with tabs[1]:
        st.subheader("数据可视化")
        
        if "basic_info" in latest_result and "字节数组" in latest_result["basic_info"]:
            bytes_data = latest_result["basic_info"]["字节数组"]
            
            # 创建两个图表
            col1, col2 = st.columns(2)
            
            with col1:
                # 字节值分布图
                fig1, ax1 = plt.subplots(figsize=(8, 4))
                ax1.bar(range(len(bytes_data)), bytes_data, alpha=0.7, color='skyblue')
                ax1.set_xlabel('字节位置')
                ax1.set_ylabel('字节值 (0-255)')
                ax1.set_title('字节值分布')
                ax1.grid(True, alpha=0.3)
                st.pyplot(fig1)
            
            with col2:
                # 字节值热力图
                if len(bytes_data) > 1:
                    fig2, ax2 = plt.subplots(figsize=(8, 4))
                    im = ax2.imshow([bytes_data], cmap='viridis', aspect='auto')
                    ax2.set_xlabel('字节位置')
                    ax2.set_title('字节值热力图')
                    plt.colorbar(im, ax=ax2)
                    st.pyplot(fig2)
            
            # 二进制位可视化
            st.subheader("二进制位视图")
            binary_matrix = []
            for byte in bytes_data:
                binary_matrix.append([int(bit) for bit in format(byte, '08b')])
            
            if binary_matrix:
                fig3, ax3 = plt.subplots(figsize=(10, max(2, len(binary_matrix) * 0.3)))
                ax3.imshow(binary_matrix, cmap='binary', aspect='auto')
                ax3.set_xlabel('位位置 (0-7)')
                ax3.set_ylabel('字节位置')
                ax3.set_title('二进制位图 (1=设置, 0=清除)')
                ax3.set_xticks(range(8))
                ax3.set_xticklabels([f'Bit {i}' for i in range(7, -1, -1)])
                st.pyplot(fig3)
    
    with tabs[2]:
        st.subheader("详细解析结果")
        
        # 显示所有解析结果
        for category, data in latest_result.items():
            if category not in ["timestamp", "original_input"]:
                with st.expander(f"📁 {category.replace('_', ' ').title()}", expanded=True):
                    if isinstance(data, dict):
                        if "错误" in data:
                            st.error(data["错误"])
                        else:
                            for key, value in data.items():
                                if isinstance(value, list) and len(value) > 10:
                                    st.write(f"**{key}:**")
                                    st.write(f"`{value[:10]}...` (显示前10个，共{len(value)}个)")
                                else:
                                    st.write(f"**{key}:** `{value}`")
                    else:
                        st.write(data)
    
    with tabs[3]:
        st.subheader("数据导出")
        
        # 导出选项
        export_format = st.selectbox("选择导出格式", ["JSON", "CSV", "文本报告"])
        
        if export_format == "JSON":
            json_data = json.dumps(
                latest_result, 
                indent=2, 
                default=str,  # 处理Timestamp对象
                ensure_ascii=False
            )
            st.download_button(
                label="📥 下载JSON",
                data=json_data,
                file_name=f"hex_parse_{latest_result['timestamp'].strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
            st.code(json_data, language="json")
        
        elif export_format == "CSV":
            # 创建扁平化的数据
            flat_data = {}
            for category, data in latest_result.items():
                if isinstance(data, dict):
                    for key, value in data.items():
                        if isinstance(value, (list, dict)):
                            flat_data[f"{category}_{key}"] = str(value)
                        else:
                            flat_data[f"{category}_{key}"] = value
                else:
                    flat_data[category] = data
            
            df = pd.DataFrame([flat_data])
            csv_data = df.to_csv(index=False)
            st.download_button(
                label="📥 下载CSV",
                data=csv_data,
                file_name=f"hex_parse_{latest_result['timestamp'].strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
            st.dataframe(df)

# 历史记录
if len(st.session_state.parsed_results) > 1:
    with st.expander("📜 解析历史"):
        history_data = []
        for i, result in enumerate(st.session_state.parsed_results):
            history_data.append({
                "序号": i + 1,
                "时间": result["timestamp"].strftime("%H:%M:%S"),
                "数据长度": len(HexParser.clean_hex_string(result["original_input"])) // 2,
                "输入预览": result["original_input"][:20] + "..." if len(result["original_input"]) > 20 else result["original_input"]
            })
        
        history_df = pd.DataFrame(history_data)
        st.dataframe(history_df, use_container_width=True)
        
        if st.button("清除历史记录"):
            st.session_state.parsed_results = []
            st.rerun()

# 使用技巧
with st.expander("💡 使用技巧"):
    st.markdown("""
    **十六进制格式支持:**
    - 带空格: `48 65 6C 6C 6F`
    - 不带空格: `48656C6C6F`
    - 带0x前缀: `0x48 0x65 0x6C`
    - 混合格式: `0x48 65 0x6C 6C 6F`
    
    **常见用途:**
    - 网络协议分析
    - 嵌入式系统调试
    - 文件格式解析
    - 数据转换验证
    
    **解析提示:**
    - 整数和浮点数会尝试大端序和小端序两种格式
    - 字符串解析会尝试多种编码
    - 特定格式会自动识别（MAC、IP、颜色等）
    """)

# CSS样式
st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
    .hex-byte {
        font-family: 'Courier New', monospace;
        background-color: #e0e0e0;
        padding: 2px 4px;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)


