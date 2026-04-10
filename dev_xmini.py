import streamlit as st
import ctypes

def parse_array_data(bytes_data) :
    # return results
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  #等宽列
    err1, err2, err3, err4 = st.columns([1, 1, 1, 1])
    sig1, sig2, sig3, sig4 = st.columns([1, 1, 1, 1])
    for i, nData in enumerate(bytes_data):
        if i==0:
            with col1:
                if int(nData) == 0:
                    msg_value = "🟠手动"
                elif int(nData) == 1:
                    msg_value = "🟢自动"
                else:
                    msg_value = "🔵老化"
                st.write("整机模式 : " + msg_value)
        elif i==1:
            with col2:
                if int(nData) == 0:
                    msg_value = "未初始化"
                elif int(nData) == 1:
                    msg_value = "初始化中"
                elif int(nData) == 2:
                    msg_value = "初始化完成"
                elif int(nData) == 3:
                    msg_value = "空闲"
                elif int(nData) == 4:
                    msg_value = "运行中"
                elif int(nData) == 5:
                    msg_value = "固件升级中"
                elif int(nData) == 6:
                    msg_value = "🔴异常"    
                else:
                    msg_value = "其他"
                st.write("整机状态 : " + msg_value)
        elif i==2:
            with col3:
                if int(nData) == 0:
                    msg_value = "未初始化"
                elif int(nData) == 1:
                    msg_value = "初始化中"
                elif int(nData) == 2:
                    msg_value = "初始化完成"
                elif int(nData) == 3:
                    msg_value = "空闲"
                elif int(nData) == 4:
                    msg_value = "运行中"
                elif int(nData) == 5:
                    msg_value = "固件升级中"
                elif int(nData) == 6:
                    msg_value = "🔴异常"    
                else:
                    msg_value = "其他"
                st.write("冷柜天车状态 : " + msg_value)
        elif i==3:
            with col4:
                if int(nData) == 0:
                    msg_value = "未初始化"
                elif int(nData) == 1:
                    msg_value = "初始化中"
                elif int(nData) == 2:
                    msg_value = "初始化完成"
                elif int(nData) == 3:
                    msg_value = "空闲"
                elif int(nData) == 4:
                    msg_value = "运行中"
                elif int(nData) == 5:
                    msg_value = "固件升级中"
                elif int(nData) == 6:
                    msg_value = "🔴异常"    
                else:
                    msg_value = "其他"
                st.write("副柜天车状态 : " + msg_value)
        elif i==4:
            with col1:
                if int(nData) == 0:
                    msg_value = "未初始化"
                elif int(nData) == 1:
                    msg_value = "初始化中"
                elif int(nData) == 2:
                    msg_value = "初始化完成"
                elif int(nData) == 3:
                    msg_value = "空闲"
                elif int(nData) == 4:
                    msg_value = "运行中"
                elif int(nData) == 5:
                    msg_value = "固件升级中"
                elif int(nData) == 6:
                    msg_value = "🔴异常"    
                else:
                    msg_value = "其他"
                st.write("打包出餐模组状态 : " + msg_value)
        elif i==16: #16~17 (原28~29)
            with col2:
                st.write(f"冷柜温度 : {ctypes.c_int16(nData*256 + bytes_data[i+1]).value}")
        elif i==45: #45~46 (原57~58)
            with col3:
                st.write(f"调料柜温度 : {ctypes.c_int16(nData*256 + bytes_data[i+1]).value}")
        elif i==41:
            with col4:
                if int(nData) == 0:
                    msg_value = "空闲"
                elif int(nData) == 1:
                    msg_value = "制作中"
                elif int(nData) == 2:
                    msg_value = "预留"
                elif int(nData) == 3:
                    msg_value = "停止"
                elif int(nData) == 4:
                    msg_value = "预留"
                elif int(nData) == 5:
                    msg_value = "预留"
                elif  int(nData) == 6:
                    msg_value = "异常"
                elif  int(nData) == 9:
                    msg_value = "预留"
                elif  int(nData) == 10:
                    msg_value = "微波漏波"
                else:
                    msg_value = "预留"
                st.write("微波仓状态 : " + msg_value)
        elif i==42:
            with col1:
                if int(nData) == 0:
                    msg_value = "已关闭"
                elif int(nData) == 1:
                    msg_value = "关闭中"
                elif int(nData) == 2:
                    msg_value = "开启中"
                elif int(nData) == 3:
                    msg_value = "已开启"
                elif int(nData) == 4:
                    msg_value = "关门失败"
                elif int(nData) == 5:
                    msg_value = "开门失败"
                else:
                    msg_value = "停止"
                st.write("微波门状态 : " + msg_value)
        elif i==43: #43~44 (原55~56)
            with col2:
                st.write(f"微波制作剩余时间 : {nData*256 + bytes_data[i+1]}")
        elif i==47: #微波1号电源故障码 (原59)
            with col3:
                if int(nData) == 0:
                    msg_value = "无故障"
                elif int(nData) == 1:
                    msg_value = "欠压保护"
                elif int(nData) == 2:
                    msg_value = "过流保护"
                elif int(nData) == 3:
                    msg_value = "过温保护"
                elif int(nData) == 4:
                    msg_value = "开路保护"
                else:
                    msg_value = "其他"
                st.write("微波1号电源故障码 : " + msg_value)
        elif i==48: #微波2号电源故障码 (原60)
            with col4:
                if int(nData) == 0:
                    msg_value = "无故障"
                elif int(nData) == 1:
                    msg_value = "欠压保护"
                elif int(nData) == 2:
                    msg_value = "过流保护"
                elif int(nData) == 3:
                    msg_value = "过温保护"
                elif int(nData) == 4:
                    msg_value = "开路保护"
                else:
                    msg_value = "其他"
                st.write("微波2号电源故障码 : " + msg_value)
        elif i==49: #微波电源通信状态
            with col1:
                if int(nData) == 0:
                    msg_value = "正常"
                else:
                    msg_value = "异常"
                st.write("微波电源通信状态 : " + msg_value)
        elif i==50: #冷柜调料柜门光栅状态
            with col2:
                if int(nData) == 0:
                    msg_value = "未触发"
                else:
                    msg_value = "触发"
                st.write("冷调料柜门 : " + msg_value)
        elif i==19: #18~40 (原30~52)
            with err1:
                st.markdown("<span style='color:red'>----------冷柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "读取冷柜数据异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "保存冷柜数据异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "冷柜天车X轴回原异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "冷柜天车Y轴回原异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "冷柜天车Y轴驱动器报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "侧门打开异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "侧门关闭异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "冷柜天车侧推电机推出异常"
                st.write(msg_value)
        elif i==20: #18~40 (原30~52)
            with err2:
                st.markdown("<span style='color:red'>----------冷柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "冷柜天车侧推电机缩回异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "破搭边异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "冷柜天车X轴位置异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "冷柜天车Y轴位置异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "等待中转组件避让超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "中转组件来接盒位超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "中转组件去送盒位启动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "中转组件去送盒位超时"
                st.write(msg_value)
        elif i==21: #18~40 (原30~52)
            with err3:
                st.markdown("<span style='color:red'>----------冷柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "中转组件低位传感器异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "中转组件来接盒位启动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "开冷柜侧门启动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("🔴" if (bytes_data[i+1] & 0x40) > 0 else "🟢") + "冷柜超时异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        elif i==28: #18~40 (原30~52)
            with err4:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "副柜天车夹盒电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "副柜天车夹盒电机张开超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "副柜天车夹盒电机闭合超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "副柜天车Y轴电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "副柜天车Y轴回原超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "副柜天车叉子电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "副柜天车叉子回原超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "直线模组电机报警"
                st.write(msg_value)
        elif i==29: #18~40 (原30~52)
            with err1:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "直线模组回原超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "暂存模组电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "暂存模组左移超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "暂存模组右移超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "左餐具运动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "左餐具取空"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "左餐具库存预警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "右餐具运动超时"
                st.write(msg_value)
        elif i==30: #18~40 (原30~52)
            with err2:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "右餐具取空"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "右餐具库存预警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "调料货道0电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "调料货道0运动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "调料货道1电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "调料货道1运动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "调料货道2电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "调料货道2运动超时"
                st.write(msg_value)
        elif i==31: #18~40 (原30~52)
            with err3:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "调料货道3电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "调料货道3运动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "调料货道4电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "调料货道4运动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "调料货道5电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "调料货道5运动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "调料货道6电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "调料货道6运动超时"
                st.write(msg_value)
        elif i==32: #18~40 (原30~52)
            with err4:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "调料货道7电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "调料货道7运动超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "调料柜门电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "调料柜门开门超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "调料柜门关门超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "拿调料超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "读副柜flash坐标失败"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "写副柜flash坐标失败"
                st.write(msg_value)
        elif i==33: #30~52
            with err1:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "副柜天车目标位取盒失败"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "副柜天车目标位送盒失败"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "副柜天车叉子顶住"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "副柜天车餐盒挤压变形"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "副柜复位失败"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "副柜x轴电机报警"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "副柜x轴回原超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "副柜天车y轴位置异常"
                st.write(msg_value)
        elif i==34: #30~52
            with err2:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "副柜天车叉子位置异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "副柜天车x轴位置异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "直线模组位置异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "餐盒类型错误"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "微波仓开门超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "微波仓关门超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "微波漏波异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        elif i==37: #30~52
            with err3:
                st.markdown("<span style='color:red'>----------打包模组异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "出餐电机伸出超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "出餐电机回原超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "出餐电机故障"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "吸盘电机下降超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "吸盘电机回原超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "吸盘电机故障"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "餐门打开超时"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "餐门关闭超时"
                st.write(msg_value)
        elif i==38: #30~52
            with err4:
                st.markdown("<span style='color:red'>----------打包模组异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "出餐电机原点传感器异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "出餐电机限位传感器异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "出餐电机所有传感器异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "吸盘电机原点传感器异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "吸盘电机限位传感器异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "吸盘电机所有传感器异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "餐门原点传感器异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "餐门限位传感器异常"
                st.write(msg_value)
        elif i==39: #30~52
            with err1:
                st.markdown("<span style='color:red'>----------打包模组异常码----------</span>", unsafe_allow_html=True)
                msg_value = ("🔴" if (nData & 0x01) > 0 else "🟢") + "餐门所有传感器异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x02) > 0 else "🟢") + "打包袋为空"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x04) > 0 else "🟢") + "吸打包袋失败"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x08) > 0 else "🟢") + "放打包袋失败"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x10) > 0 else "🟢") + "写内存异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x20) > 0 else "🟢") + "读内存异常"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x40) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("🔴" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        elif i==5: #17~27 bit signal
            with sig1:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "调料柜门上限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "调料柜门下限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "调料柜门安全光栅"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "冷柜天车侧推右限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "冷柜天车侧推左限位(原点)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "冷柜天车餐盒姿态传感器(内)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "冷柜天车中间传感器(中)"
                st.write(msg_value)
        elif i==6: #17~27 bit signal
            with sig2:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "冷柜天车餐盒到位传感器(外)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "冷柜X轴左限位(原点)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "冷柜X轴右限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "冷柜门控开关"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "冷柜Y轴下限位(原点)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "冷柜Y轴上限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        elif i==7: #17~27 bit signal
            with sig3:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "吸盘升降上限位(原点)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "吸盘升降下限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "吸纸检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "纸仓预警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "缺纸检测(预留)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "出餐电机前区域检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "出餐电机前限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "出餐电机后限位(原点)"
                st.write(msg_value)
        elif i==8: #17~27 bit signal
            with sig4:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "餐盒取走检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "左餐具预警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "右餐具预警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "左餐具检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "右餐具检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        elif i==9: #17~27 bit signal
            with sig1:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "中转组件前限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "中转组件后限位(原点)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "中转组件高位餐盒检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "中转组件低位餐盒检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "上层暂存位左检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "上层暂存位右检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "下层暂存位左检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "下层暂存位右检测"
                st.write(msg_value)
        elif i==10: #17~27 bit signal
            with sig2:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "暂存平台左限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "暂存平台右限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        elif i==11: #17~27 bit signal
            with sig3:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "副柜天车Y轴上限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "副柜天车Y轴下限位(原点)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "副柜天车叉子前限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "副柜天车叉子后限位(原点)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "副柜天车夹盒电机张开(原点)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "副柜天车夹盒电机夹紧限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "副柜天车餐盒检测"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "副柜门控开关"
                st.write(msg_value)
        elif i==12: #17~27 bit signal
            with sig4:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "副柜取餐门安全光栅"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "副柜取餐门防夹手微动开关"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "副柜取餐门关门限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "副柜取餐门开门限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        elif i==13: #17~27 bit signal
            with sig1:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "冷柜侧门关门传感器"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "冷柜侧门开门传感器"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "冷柜Y轴驱动报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "副柜天车Y轴驱动报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "冷柜X轴驱动报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "吸盘升降电机驱动报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "中转直线运动模组驱动报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "出餐平台电机驱动报警"
                st.write(msg_value)
        elif i==14: #17~27 bit signal
            with sig2:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "副柜天车叉子电机驱动报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "调料货道光栅"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "调料柜货道信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        elif i==15: #17~27 bit signal
            with sig3:
                st.markdown("<span style='color:blue'>----------传感器信号----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "左餐具电机位置信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "右餐具电机位置信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "微波门上限(关)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "微波门下限(开)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        

    return {"finish"}

