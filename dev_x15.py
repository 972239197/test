import streamlit as st
import ctypes

def parse_array_data(bytes_data) :
    # return results
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  #等宽列
    err1, err2, err3, err4 = st.columns([1, 1, 1, 1])
    sig1, sig2, sig3, sig4 = st.columns([1, 1, 1, 1])
    for i, nData in enumerate(bytes_data):
        if i==12:
            with col1:
                if int(nData) == 0:
                    msg_value = "🔴手动"
                elif int(nData) == 1:
                    msg_value = "🟢自动"
                else:
                    msg_value = "🔵老化"
                st.write("整机模式 : " + msg_value)
        elif i==13:
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
                else:
                    msg_value = "异常"
                st.write("整机状态 : " + msg_value)
        elif i==14:
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
                else:
                    msg_value = "异常"
                st.write("冷柜天车状态 : " + msg_value)
        elif i==15:
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
                else:
                    msg_value = "异常"
                st.write("副柜天车状态 : " + msg_value)
        elif i==16:
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
                else:
                    msg_value = "异常"
                st.write("打包出餐模组状态 : " + msg_value)
        elif i==17:
            with col2:
                st.write(f"冷柜温度 : {ctypes.c_int16(nData*256 + bytes_data[i+1]).value}")
        elif i==19:
            with col3:
                st.write(f"调料柜温度 : {ctypes.c_int16(nData*256 + bytes_data[i+1]).value}")
        elif i==21:
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
        elif i==22:
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
        elif i==23: #23~24
            with col2:
                st.write(f"微波制作剩余时间 : {nData*256 + bytes_data[i+1]}")
        elif i==25: #25~44
            with err1:
                st.markdown("<span style='color:red'>----------冷柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴读取冷柜数据异常" if (nData & 0x01) > 0 else "🟢读取冷柜数据异常"
                st.write(msg_value)
                msg_value = "🔴保存冷柜数据异常" if (nData & 0x02) > 0 else "🟢保存冷柜数据异常"
                st.write(msg_value)
                msg_value = "🔴冷柜天车X轴回原异常" if (nData & 0x04) > 0 else "🟢冷柜天车X轴回原异常"
                st.write(msg_value)
                msg_value = "🔴冷柜天车X轴位置异常" if (nData & 0x08) > 0 else "🟢冷柜天车X轴位置异常"
                st.write(msg_value)
                msg_value = "🔴冷柜天车X轴驱动器报警" if (nData & 0x10) > 0 else "🟢冷柜天车X轴驱动器报警"
                st.write(msg_value)
                msg_value = "🔴冷柜天车Y轴回原异常" if (nData & 0x20) > 0 else "🟢冷柜天车Y轴回原异常"
                st.write(msg_value)
                msg_value = "🔴冷柜天车Y轴位置异常" if (nData & 0x40) > 0 else "🟢冷柜天车Y轴位置异常"
                st.write(msg_value)
                msg_value = "🔴冷柜天车Y轴驱动器报警" if (nData & 0x80) > 0 else "🟢冷柜天车Y轴驱动器报警"
                st.write(msg_value)
        elif i==26: #25~44
            with err2:
                st.markdown("<span style='color:red'>----------冷柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴冷柜天车侧推电机推出异常" if (nData & 0x01) > 0 else "🟢冷柜天车侧推电机推出异常"
                st.write(msg_value)
                msg_value = "🔴冷柜天车侧推电机缩回异常" if (nData & 0x02) > 0 else "🟢冷柜天车侧推电机缩回异常"
                st.write(msg_value)
                msg_value = "🔴开冷柜侧门异常" if (nData & 0x04) > 0 else "🟢开冷柜侧门异常"
                st.write(msg_value)
                msg_value = "🔴关冷柜侧门异常" if (nData & 0x08) > 0 else "🟢关冷柜侧门异常"
                st.write(msg_value)
                msg_value = "🔴冷柜天车餐盒破搭边异常" if (nData & 0x10) > 0 else "🟢冷柜天车餐盒破搭边异常"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x20) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x40) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴中转直线运动模组回原点错误" if (nData & 0x80) > 0 else "🟢中转直线运动模组回原点错误"
                st.write(msg_value)
        elif i==27: #25~44
            with err3:
                st.markdown("\n<span style='color:red'>----------冷柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴中转直线运动模组位置错误" if (nData & 0x01) > 0 else "🟢中转直线运动模组位置错误"
                st.write(msg_value)
                msg_value = "🔴中转直线运动模组驱动器报警" if (nData & 0x02) > 0 else "🟢中转直线运动模组驱动器报警"
                st.write(msg_value)
                msg_value = "🔴中转旋转运动模组回原点错误" if (nData & 0x04) > 0 else "🟢中转旋转运动模组回原点错误"
                st.write(msg_value)
                msg_value = "🔴中转旋转运动模组位置错误" if (nData & 0x08) > 0 else "🟢中转旋转运动模组位置错误"
                st.write(msg_value)
                msg_value = "🔴中转旋转运动模组驱动器报警" if (nData & 0x10) > 0 else "🟢中转旋转运动模组驱动器报警"
                st.write(msg_value)
                msg_value = "🔴中转组件高位信号触发超时" if (nData & 0x20) > 0 else "🟢中转组件高位信号触发超时"
                st.write(msg_value)
                msg_value = "🔴中转组件低位信号触发超时" if (nData & 0x40) > 0 else "🟢中转组件低位信号触发超时"
                st.write(msg_value)
                msg_value = "🔴副柜天车叉子后限位不触发超时" if (nData & 0x80) > 0 else "🟢副柜天车叉子后限位不触发超时"
                st.write(msg_value)
        elif i==28: #25~44
            with err4:
                st.markdown("\n<span style='color:red'>----------冷柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴中转组件来就绪位超时" if (nData & 0x01) > 0 else "🟢中转组件来就绪位超时"
                st.write(msg_value)
                msg_value = "🔴中转直线运动模右移超时" if (nData & 0x02) > 0 else "🟢中转直线运动模右移超时"
                st.write(msg_value)
                msg_value = "🔴中转组件上餐盒类型错误" if (nData & 0x04) > 0 else "🟢中转组件上餐盒类型错误"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x08) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x10) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x20) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x40) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴冷柜天车超时异常" if (nData & 0x80) > 0 else "🟢冷柜天车超时异常"
                st.write(msg_value)
        elif i==31: #25~44
            with err1:
                st.markdown("<span style='color:red'>----------冷柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴调料柜门开门超时" if (nData & 0x01) > 0 else "🟢调料柜门开门超时"
                st.write(msg_value)
                msg_value = "🔴调料柜门关门超时" if (nData & 0x02) > 0 else "🟢调料柜门关门超时"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x04) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x08) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x10) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x20) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x40) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x80) > 0 else "🟢预留"
                st.write(msg_value)
        elif i==32: #25~44
            with err2:
                st.markdown("<span style='color:red'>----------冷柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴弹簧货道1超时" if (nData & 0x01) > 0 else "🟢弹簧货道1超时"
                st.write(msg_value)
                msg_value = "🔴弹簧货道2超时" if (nData & 0x02) > 0 else "🟢弹簧货道2超时"
                st.write(msg_value)
                msg_value = "🔴弹簧货道3超时" if (nData & 0x04) > 0 else "🟢弹簧货道3超时"
                st.write(msg_value)
                msg_value = "🔴弹簧货道4超时" if (nData & 0x08) > 0 else "🟢弹簧货道4超时"
                st.write(msg_value)
                msg_value = "🔴弹簧货道5超时" if (nData & 0x10) > 0 else "🟢弹簧货道5超时"
                st.write(msg_value)
                msg_value = "🔴弹簧货道6超时" if (nData & 0x20) > 0 else "🟢弹簧货道6超时"
                st.write(msg_value)
                msg_value = "🔴弹簧货道7超时" if (nData & 0x40) > 0 else "🟢弹簧货道7超时"
                st.write(msg_value)
                msg_value = "🔴弹簧货道8超时" if (nData & 0x80) > 0 else "🟢弹簧货道8超时"
                st.write(msg_value)
        elif i==33: #25~44
            with err3:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴副柜天车叉子电机伸出超时" if (nData & 0x01) > 0 else "🟢副柜天车叉子电机伸出超时"
                st.write(msg_value)
                msg_value = "🔴副柜天车叉子电机缩回超时" if (nData & 0x02) > 0 else "🟢副柜天车叉子电机缩回超时"
                st.write(msg_value)
                msg_value = "🔴副柜X轴电机左移超时" if (nData & 0x04) > 0 else "🟢副柜X轴电机左移超时"
                st.write(msg_value)
                msg_value = "🔴副柜X轴电机右移超时" if (nData & 0x08) > 0 else "🟢副柜X轴电机右移超时"
                st.write(msg_value)
                msg_value = "🔴副柜Y轴电机下降超时" if (nData & 0x10) > 0 else "🟢副柜Y轴电机下降超时"
                st.write(msg_value)
                msg_value = "🔴副柜Y轴电机上升超时" if (nData & 0x20) > 0 else "🟢副柜Y轴电机上升超时"
                st.write(msg_value)
                msg_value = "🔴副柜天车夹盒电机张开超时" if (nData & 0x40) > 0 else "🟢副柜天车夹盒电机张开超时"
                st.write(msg_value)
                msg_value = "🔴副柜天车夹盒电机闭合超时" if (nData & 0x80) > 0 else "🟢副柜天车夹盒电机闭合超时"
                st.write(msg_value)
        elif i==34: #25~44
            with err4:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴微波门打开超时" if (nData & 0x01) > 0 else "🟢微波门打开超时"
                st.write(msg_value)
                msg_value = "🔴微波门关闭超时" if (nData & 0x02) > 0 else "🟢微波门关闭超时"
                st.write(msg_value)
                msg_value = "🔴副柜天车叉子电机传感器异常" if (nData & 0x04) > 0 else "🟢副柜天车叉子电机传感器异常"
                st.write(msg_value)
                msg_value = "🔴副柜X轴电机传感器异常" if (nData & 0x08) > 0 else "🟢副柜X轴电机传感器异常"
                st.write(msg_value)
                msg_value = "🔴副柜Y轴电机传感器异常" if (nData & 0x10) > 0 else "🟢副柜Y轴电机传感器异常"
                st.write(msg_value)
                msg_value = "🔴副柜天车夹盒电机传感器异常" if (nData & 0x20) > 0 else "🟢副柜天车夹盒电机传感器异常"
                st.write(msg_value)
                msg_value = "🔴微波门传感器异常" if (nData & 0x40) > 0 else "🟢微波门传感器异常"
                st.write(msg_value)
                msg_value = "🔴副柜天车叉子电机位置异常" if (nData & 0x80) > 0 else "🟢副柜天车叉子电机位置异常"
                st.write(msg_value)
        elif i==35: #25~44
            with err1:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴副柜X轴电机位置异常" if (nData & 0x01) > 0 else "🟢副柜X轴电机位置异常"
                st.write(msg_value)
                msg_value = "🔴副柜Y轴电机位置异常" if (nData & 0x02) > 0 else "🟢副柜Y轴电机位置异常"
                st.write(msg_value)
                msg_value = "🔴副柜天车取餐盒失败" if (nData & 0x04) > 0 else "🟢副柜天车取餐盒失败"
                st.write(msg_value)
                msg_value = "🔴副柜天车放餐盒失败" if (nData & 0x08) > 0 else "🟢副柜天车放餐盒失败"
                st.write(msg_value)
                msg_value = "🔴副柜天车叉子取餐盒为空" if (nData & 0x10) > 0 else "🟢副柜天车叉子取餐盒为空"
                st.write(msg_value)
                msg_value = "🔴副柜天车叉子放餐盒滞留" if (nData & 0x20) > 0 else "🟢副柜天车叉子放餐盒滞留"
                st.write(msg_value)
                msg_value = "🔴副柜天车叉子变形" if (nData & 0x40) > 0 else "🟢副柜天车叉子变形"
                st.write(msg_value)
                msg_value = "🔴副柜天车去目标失败" if (nData & 0x80) > 0 else "🟢副柜天车去目标失败"
                st.write(msg_value)
        elif i==36: #25~44
            with err2:
                st.markdown("<span style='color:red'>----------副柜异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴副柜写内存异常" if (nData & 0x01) > 0 else "🟢副柜写内存异常"
                st.write(msg_value)
                msg_value = "🔴副柜读内存异常" if (nData & 0x02) > 0 else "🟢副柜读内存异常"
                st.write(msg_value)
                msg_value = "🔴副柜天车复位失败" if (nData & 0x04) > 0 else "🟢副柜天车复位失败"
                st.write(msg_value)
                msg_value = "🔴副柜X轴电机故障" if (nData & 0x08) > 0 else "🟢副柜X轴电机故障"
                st.write(msg_value)
                msg_value = "🔴副柜Y轴电机故障" if (nData & 0x10) > 0 else "🟢副柜Y轴电机故障"
                st.write(msg_value)
                msg_value = "🔴叉子电机故障" if (nData & 0x20) > 0 else "🟢叉子电机故障"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x40) > 0 else "🟢预留"
                st.write(msg_value)
                msg_value = "🔴预留" if (nData & 0x80) > 0 else "🟢预留"
                st.write(msg_value)
        elif i==41: #25~44
            with err3:
                st.markdown("<span style='color:red'>----------打包模组异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴打包上下移电机下降超时" if (nData & 0x01) > 0 else "🟢打包上下移电机下降超时"
                st.write(msg_value)
                msg_value = "🔴打包上下移电机上升超时" if (nData & 0x02) > 0 else "🟢打包上下移电机上升超时"
                st.write(msg_value)
                msg_value = "🔴出餐电机伸出超时" if (nData & 0x04) > 0 else "🟢出餐电机伸出超时"
                st.write(msg_value)
                msg_value = "🔴出餐电机缩回超时" if (nData & 0x08) > 0 else "🟢出餐电机缩回超时"
                st.write(msg_value)
                msg_value = "🔴左出餐具取空" if (nData & 0x10) > 0 else "🟢左出餐具取空"
                st.write(msg_value)
                msg_value = "🔴右出餐具取空" if (nData & 0x20) > 0 else "🟢右出餐具取空"
                st.write(msg_value)
                msg_value = "🔴吸盘电机下降超时" if (nData & 0x40) > 0 else "🟢吸盘电机下降超时"
                st.write(msg_value)
                msg_value = "🔴吸盘电机上升超时" if (nData & 0x80) > 0 else "🟢吸盘电机上升超时"
                st.write(msg_value)
        elif i==42: #25~44
            with err4:
                st.markdown("<span style='color:red'>----------打包模组异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴吸盘电机左移超时" if (nData & 0x01) > 0 else "🟢吸盘电机左移超时"
                st.write(msg_value)
                msg_value = "🔴吸盘电机右移超时" if (nData & 0x02) > 0 else "🟢吸盘电机右移超时"
                st.write(msg_value)
                msg_value = "🔴托盘电机伸出超时" if (nData & 0x04) > 0 else "🟢托盘电机伸出超时"
                st.write(msg_value)
                msg_value = "🔴托盘电机缩回超时" if (nData & 0x08) > 0 else "🟢托盘电机缩回超时"
                st.write(msg_value)
                msg_value = "🔴夹手电机张开超时" if (nData & 0x10) > 0 else "🟢夹手电机张开超时"
                st.write(msg_value)
                msg_value = "🔴夹手电机关闭超时" if (nData & 0x20) > 0 else "🟢夹手电机关闭超时"
                st.write(msg_value)
                msg_value = "🔴纸盒仓推杆电机前进超时" if (nData & 0x40) > 0 else "🟢纸盒仓推杆电机前进超时"
                st.write(msg_value)
                msg_value = "🔴纸盒仓推杆电机后退超时" if (nData & 0x80) > 0 else "🟢纸盒仓推杆电机后退超时"
                st.write(msg_value)
        elif i==43: #25~44
            with err1:
                st.markdown("<span style='color:red'>----------打包模组异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴打包上下移电机传感器异常" if (nData & 0x01) > 0 else "🟢打包上下移电机传感器异常"
                st.write(msg_value)
                msg_value = "🔴出餐电机传感器异常" if (nData & 0x02) > 0 else "🟢出餐电机传感器异常"
                st.write(msg_value)
                msg_value = "🔴中间出餐具取空" if (nData & 0x04) > 0 else "🟢中间出餐具取空"
                st.write(msg_value)
                msg_value = "🔴吸盘电机升降传感器异常" if (nData & 0x08) > 0 else "🟢吸盘电机升降传感器异常"
                st.write(msg_value)
                msg_value = "🔴吸盘电机前后传感器异常" if (nData & 0x10) > 0 else "🟢吸盘电机前后传感器异常"
                st.write(msg_value)
                msg_value = "🔴托盘电机传感器异常" if (nData & 0x20) > 0 else "🟢托盘电机传感器异常"
                st.write(msg_value)
                msg_value = "🔴夹手电机传感器异常" if (nData & 0x40) > 0 else "🟢夹手电机传感器异常"
                st.write(msg_value)
                msg_value = "🔴纸盒推杆电机传感器异常" if (nData & 0x80) > 0 else "🟢纸盒推杆电机传感器异常"
                st.write(msg_value)
        elif i==44: #25~44
            with err2:
                st.markdown("<span style='color:red'>----------打包模组异常码----------</span>", unsafe_allow_html=True)
                msg_value = "🔴打包上下移电机位置异常" if (nData & 0x01) > 0 else "🟢打包上下移电机位置异常"
                st.write(msg_value)
                msg_value = "🔴打包袋为空" if (nData & 0x02) > 0 else "🟢打包袋为空"
                st.write(msg_value)
                msg_value = "🔴吸打包袋失败" if (nData & 0x04) > 0 else "🟢吸打包袋失败"
                st.write(msg_value)
                msg_value = "🔴下放餐盒失败" if (nData & 0x08) > 0 else "🟢下放餐盒失败"
                st.write(msg_value)
                msg_value = "🔴推出餐盒失败" if (nData & 0x10) > 0 else "🟢推出餐盒失败"
                st.write(msg_value)
                msg_value = "🔴打包模组写内存异常" if (nData & 0x20) > 0 else "🟢打包模组写内存异常"
                st.write(msg_value)
                msg_value = "🔴打包模组读内存异常" if (nData & 0x40) > 0 else "🟢打包模组读内存异常"
                st.write(msg_value)
                msg_value = "🔴打包模组复位失败" if (nData & 0x80) > 0 else "🟢打包模组复位失败"
                st.write(msg_value)
        elif i==45: #45~57 bit signal
            with sig1:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = "⚫"+"调料柜门上限位" if (nData & 0x01) > 0 else "🟢"+"调料柜门上限位"
                st.write(msg_value)
                msg_value = "⚫"+"调料柜门下限位" if (nData & 0x02) > 0 else "🟢"+"调料柜门下限位"
                st.write(msg_value)
                msg_value = "⚫"+"调料柜货道光纤" if (nData & 0x04) > 0 else "🟢"+"调料柜货道光纤"
                st.write(msg_value)
                msg_value = "⚫"+"调料柜门安全光栅" if (nData & 0x08) > 0 else "🟢"+"调料柜门安全光栅"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜天车侧推右限" if (nData & 0x10) > 0 else "🟢"+"冷柜天车侧推右限"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜天车侧推左限位(原点)" if (nData & 0x20) > 0 else "🟢"+"冷柜天车侧推左限位(原点)"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜天车餐盒姿态传感器(内)" if (nData & 0x40) > 0 else "🟢"+"冷柜天车餐盒姿态传感器(内)"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜天车中间传感器(中)" if (nData & 0x80) > 0 else "🟢"+"冷柜天车中间传感器(中)"
                st.write(msg_value)
        elif i==46: #45~57 bit signal
            with sig2:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = "⚫"+"冷柜天车餐盒到位传感器(外)" if (nData & 0x01) > 0 else "🟢"+"冷柜天车餐盒到位传感器(外)"
                st.write(msg_value)
                msg_value = "⚫"+"预留" if (nData & 0x02) > 0 else "🟢"+"预留"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜X左限位(原点)" if (nData & 0x04) > 0 else "🟢"+"冷柜X左限位(原点)"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜X右限位" if (nData & 0x08) > 0 else "🟢"+"冷柜X右限位"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜Y上限位" if (nData & 0x10) > 0 else "🟢"+"冷柜Y上限位"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜Y下限位(原点)" if (nData & 0x20) > 0 else "🟢"+"冷柜Y下限位(原点)"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜侧门开门传感器" if (nData & 0x40) > 0 else "🟢"+"冷柜侧门开门传感器"
                st.write(msg_value)
                msg_value = "⚫"+"冷柜侧门关门传感器" if (nData & 0x80) > 0 else "🟢"+"冷柜侧门关门传感器"
                st.write(msg_value)
        elif i==47: #45~57 bit signal
            with sig3:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = "⚫"+"电动纸盒仓前限" if (nData & 0x01) > 0 else "🟢"+"电动纸盒仓前限"
                st.write(msg_value)
                msg_value = "⚫"+"电动纸盒仓后限" if (nData & 0x02) > 0 else "🟢"+"电动纸盒仓后限"
                st.write(msg_value)
                msg_value = "⚫"+"纸盒仓推板到位信号" if (nData & 0x04) > 0 else "🟢"+"纸盒仓推板到位信号"
                st.write(msg_value)
                msg_value = "⚫"+"纸盒仓防压手信号" if (nData & 0x08) > 0 else "🟢"+"纸盒仓防压手信号"
                st.write(msg_value)
                msg_value = "⚫"+"缺盒1级预警检测信号" if (nData & 0x10) > 0 else "🟢"+"缺盒1级预警检测信号"
                st.write(msg_value)
                msg_value = "⚫"+"纸盒仓关门信号" if (nData & 0x20) > 0 else "🟢"+"纸盒仓关门信号"
                st.write(msg_value)
                msg_value = "⚫"+"纸盒展开到位检测" if (nData & 0x40) > 0 else "🟢"+"纸盒展开到位检测"
                st.write(msg_value)
                msg_value = "⚫"+"出餐平台推出前限" if (nData & 0x80) > 0 else "🟢"+"出餐平台推出前限"
                st.write(msg_value)
        elif i==48: #45~57 bit signal
            with sig4:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = "⚫"+"出餐平台推出后限" if (nData & 0x01) > 0 else "🟢"+"出餐平台推出后限"
                st.write(msg_value)
                msg_value = "⚫"+"缺盒2级预警检测信号" if (nData & 0x02) > 0 else "🟢"+"缺盒2级预警检测信号"
                st.write(msg_value)
                msg_value = "⚫"+"左餐具预警" if (nData & 0x04) > 0 else "🟢"+"左餐具预警"
                st.write(msg_value)
                msg_value = "⚫"+"右餐具预警" if (nData & 0x08) > 0 else "🟢"+"右餐具预警"
                st.write(msg_value)
                msg_value = "⚫"+"左餐具检测" if (nData & 0x10) > 0 else "🟢"+"左餐具检测"
                st.write(msg_value)
                msg_value = "⚫"+"右餐具检测" if (nData & 0x20) > 0 else "🟢"+"右餐具检测"
                st.write(msg_value)
                msg_value = "⚫"+"中餐具检测" if (nData & 0x40) > 0 else "🟢"+"中餐具检测"
                st.write(msg_value)
                msg_value = "⚫"+"中餐具预警" if (nData & 0x80) > 0 else "🟢"+"中餐具预警"
                st.write(msg_value)
        elif i==49: #45~57 bit signal
            with sig1:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = "⚫"+"中转组件前限位" if (nData & 0x01) > 0 else "🟢"+"中转组件前限位"
                st.write(msg_value)
                msg_value = "⚫"+"中转组件后限位" if (nData & 0x02) > 0 else "🟢"+"中转组件后限位"
                st.write(msg_value)
                msg_value = "⚫"+"中转组件旋转前限位" if (nData & 0x04) > 0 else "🟢"+"中转组件旋转前限位"
                st.write(msg_value)
                msg_value = "⚫"+"中转组件旋转后限位" if (nData & 0x08) > 0 else "🟢"+"中转组件旋转后限位"
                st.write(msg_value)
                msg_value = "⚫"+"中转组件高位餐盒检测" if (nData & 0x10) > 0 else "🟢"+"中转组件高位餐盒检测"
                st.write(msg_value)
                msg_value = "⚫"+"中转组件低位餐盒检测" if (nData & 0x20) > 0 else "🟢"+"中转组件低位餐盒检测"
                st.write(msg_value)
                msg_value = "⚫"+"1号暂存位检测" if (nData & 0x40) > 0 else "🟢"+"1号暂存位检测"
                st.write(msg_value)
                msg_value = "⚫"+"2号暂存位检测" if (nData & 0x80) > 0 else "🟢"+"2号暂存位检测"
                st.write(msg_value)
        elif i==50: #45~57 bit signal
            with sig2:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = "⚫"+"3号暂存位检测" if (nData & 0x01) > 0 else "🟢"+"3号暂存位检测"
                st.write(msg_value)
                msg_value = "⚫"+"4号暂存位检测" if (nData & 0x02) > 0 else "🟢"+"4号暂存位检测"
                st.write(msg_value)
                msg_value = "⚫"+"5号暂存位检测" if (nData & 0x04) > 0 else "🟢"+"5号暂存位检测"
                st.write(msg_value)
                msg_value = "⚫"+"6号暂存位检测" if (nData & 0x08) > 0 else "🟢"+"6号暂存位检测"
                st.write(msg_value)
                msg_value = "⚫"+"7号暂存位检测" if (nData & 0x10) > 0 else "🟢"+"7号暂存位检测"
                st.write(msg_value)
                msg_value = "⚫"+"8号暂存位检测" if (nData & 0x20) > 0 else "🟢"+"8号暂存位检测"
                st.write(msg_value)
                msg_value = "⚫"+"9号暂存位检测" if (nData & 0x40) > 0 else "🟢"+"9号暂存位检测"
                st.write(msg_value)
                msg_value = "⚫"+"10号暂存位检测" if (nData & 0x80) > 0 else "🟢"+"10号暂存位检测"
                st.write(msg_value)
        elif i==51: #45~57 bit signal
            with sig3:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = "⚫"+"副柜天车Y轴上限位" if (nData & 0x01) > 0 else "🟢"+"副柜天车Y轴上限位"
                st.write(msg_value)
                msg_value = "⚫"+"副柜天车Y轴下限位(原点)" if (nData & 0x02) > 0 else "🟢"+"副柜天车Y轴下限位(原点)"
                st.write(msg_value)
                msg_value = "⚫"+"副柜天车叉子前限位" if (nData & 0x04) > 0 else "🟢"+"副柜天车叉子前限位"
                st.write(msg_value)
                msg_value = "⚫"+"副柜天车叉子后限位(原点)" if (nData & 0x08) > 0 else "🟢"+"副柜天车叉子后限位(原点)"
                st.write(msg_value)
                msg_value = "⚫"+"副柜天车夹盒电机张开限位(原点)" if (nData & 0x10) > 0 else "🟢"+"副柜天车夹盒电机张开限位(原点)"
                st.write(msg_value)
                msg_value = "⚫"+"副柜天车夹盒电机夹紧限位" if (nData & 0x20) > 0 else "🟢"+"副柜天车夹盒电机夹紧限位"
                st.write(msg_value)
                msg_value = "⚫"+"副柜天车餐盒检测" if (nData & 0x40) > 0 else "🟢"+"副柜天车餐盒检测"
                st.write(msg_value)
                msg_value = "⚫"+"叉子餐盒变形检测" if (nData & 0x80) > 0 else "🟢"+"叉子餐盒变形检测"
                st.write(msg_value)
        elif i==52: #45~57 bit signal
            with sig4:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "副柜天车X轴左限位(原点)"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "副柜天车X轴右限位"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "打包接餐小托盘后限"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "打包接餐小托盘前限"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)
        elif i==53: #45~57 bit signal
            with sig1:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "真空取盒前后移前限信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "真空取盒前后移后限信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "真空取盒上下移上限信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "真空取盒上下移下限信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "真空取袋纸盒检测光眼信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "夹手上限开信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "夹手餐盒检测信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "夹手下限关信号"
                st.write(msg_value)
        elif i==54: #45~57 bit signal
            with sig2:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "夹手上下移电机上限信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "夹手上下移电机下限信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "纸盒仓前进按钮"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "纸盒仓后退按钮"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "副柜门控开关"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "调料柜货道信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "副柜中餐具电机位置信号"
                st.write(msg_value)
        elif i==55: #45~57 bit signal
            with sig3:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "副柜左餐具电机位置信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "副柜右餐具电机位置信号"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "微波门上限"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "微波门下限"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "冷柜Y轴驱动器报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "冷柜X轴驱动器报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "副柜X轴驱动器报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "副柜天车Y轴驱动器报警"
                st.write(msg_value)
        elif i==56: #45~57 bit signal
            with sig4:
                st.markdown("<span style='color:red'>----------信号传感器----------</span>", unsafe_allow_html=True)
                msg_value = ("⚫" if (nData & 0x01) > 0 else "🟢") + "中转直线运动模组驱动器报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x02) > 0 else "🟢") + "夹盒升降电机驱动器报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x04) > 0 else "🟢") + "中转模组旋转步进报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x08) > 0 else "🟢") + "副柜天车叉子步进报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x10) > 0 else "🟢") + "纸盒仓IO步进报警"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x20) > 0 else "🟢") + "冷柜门控开关"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x40) > 0 else "🟢") + "预留"
                st.write(msg_value)
                msg_value = ("⚫" if (nData & 0x80) > 0 else "🟢") + "预留"
                st.write(msg_value)

    return {"finish"}