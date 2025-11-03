import streamlit as st

def parse_array_data(bytes_data) :
    # return results
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  # 中间列宽度是两边的2倍
    for i, nData in enumerate(bytes_data):
        if i==12:
            with col1:
                if int(nData) == 0:
                    msg_value = "🔴手动"
                elif int(nData) == 1:
                    msg_value = "🟢自动"
                else:
                    msg_value = "💚老化❤️"
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
                st.write(f"冷柜温度 : {nData*256 + bytes_data[i+1]}")
        elif i==19:
            with col3:
                st.write(f"调料柜温度 : {nData*256 + bytes_data[i+1]}")
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
            with col3:
                st.write("******")
            with col4:
                st.write("******")
        elif i==25: #25~44
            with col1:
                st.markdown("<span style='color:red'>冷柜异常码--------------------</span>", unsafe_allow_html=True)
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
            with col2:
                st.markdown("<span style='color:red'>------------------------------</span>", unsafe_allow_html=True)
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
            with col3:
                st.markdown("<span style='color:red'>------------------------------</span>", unsafe_allow_html=True)
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
            with col4:
                st.markdown("<span style='color:red'>------------------------------</span>", unsafe_allow_html=True)
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
            with col1:
                st.markdown("<span style='color:red'>------------------------------</span>", unsafe_allow_html=True)
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
            with col2:
                st.markdown("<span style='color:red'>------------------------------</span>", unsafe_allow_html=True)
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

    return {"finish"}