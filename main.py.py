# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="语音声学分析工具", layout="wide")
st.title("语音声学参数分析工具")

uploaded = st.file_uploader("上传语音文件 (WAV)", type=["wav"])

if uploaded is not None:
    st.success("文件已上传：%s" % uploaded.name)
    st.audio(uploaded, format="audio/wav")

    if st.button("执行分析", type="primary"):
        import parselmouth
        from parselmouth.praat import call
        import numpy as np

        sound = parselmouth.Sound(uploaded.getvalue())
        pitch = sound.to_pitch()
        vals = [x for x in pitch.selected_array["frequency"] if x > 0]
        mean_f0 = float(np.mean(vals)) if vals else 0.0

        st.metric("基频均值 (Hz)", "%.1f" % mean_f0)
        st.metric("总时长 (秒)", "%.2f" % sound.duration)
        st.write("分析完成。")
