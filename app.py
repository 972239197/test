import streamlit as st
import pandas as pd
import numpy as np
import struct
import binascii
import re
from typing import Dict, List, Any

from io import StringIO

# 页面配置
st.set_page_config(
    page_title="数组解析工具",
    page_icon="📊",
    layout="wide"
)

# 标题和描述

# 标题和描述
st.title("🔢 十六进制数据解析器")
st.write("欢迎来到我的应用！")
st.markdown("""
这是一个强大的数组解析工具
""")

# 1. 基础多选下拉菜单
st.header("请选择设备类型")

# 选项数据
dev_type = ["Xmini", "X1.3重构", "X1.5", "Xmicrowave"]

# 多选下拉菜单
selected_dev = st.selectbox(
    "选择你要解析的设备",
    dev_type,
    index=0,  # 默认选择第一个选项
    help="默认选择 Xmini"
)

st.write(f"**你选择的设备:** {selected_dev}")



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
    
    
# 侧边栏配置
with st.sidebar:
    st.header("⚙️ 解析配置")
    parse_options = st.multiselect(
        "选择解析类型",
        ["整数类型", "字符串类型"],
        default=["整数类型"]
    )
    st.markdown("---")
    st.header("📊 示例数据")
    
    example_data = st.selectbox(
        "选择示例数据",
        ["整数示例", "字符串示例", "MAC地址", "IP地址"]
    )
    

# 主界面
st.header("📥 输入十六进制数据")

# 示例数据映射
example_map = {
    "整数示例": "DEADBEEF",
    "字符串示例": "48656C6C6F20576F726C64",
    "MAC地址": "A1B2C3D4E5F6",
    "IP地址": "C0A80101",
}

# 数据输入区域
col1, col2 = st.columns([3, 1])

with col1:
        default_hex = example_map.get(example_data, "")
        hex_input = st.text_area(
            "输入十六进制数据",
            value=default_hex,
            height=100
        )


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
            if "整数类型" in parse_options:
                results["integers"] = HexParser.parse_integers(hex_input)

            if "字符串类型" in parse_options:
                results["strings"] = HexParser.parse_strings(hex_input)

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


