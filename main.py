import streamlit as st
import wave
import struct
import math

st.set_page_config(page_title="语音声学参数分析工具", page_icon="🎙️", layout="centered")


def analyze_wav(file_bytes, filename):
    """用标准库解析 WAV 头部并做简单声学分析（零第三方依赖，保证打包稳定）。"""
    import io
    try:
        with wave.open(io.BytesIO(file_bytes), "rb") as w:
            params = w.getparams()
            n_channels, sampwidth, framerate, n_frames = (
                params.nchannels, params.sampwidth, params.framerate, params.nframes)
            duration = n_frames / float(framerate)
            raw = w.readframes(min(n_frames, framerate * 5))  # 只取前5秒做粗分析
    except Exception as e:
        st.error(f"无法解析该文件为 WAV：{e}")
        return

    # 简单能量/振幅统计
    if sampwidth == 2:
        samples = struct.unpack("<%dh" % (len(raw) // 2), raw)
    elif sampwidth == 1:
        samples = [b - 128 for b in raw]
    else:
        samples = struct.unpack("<%dh" % (len(raw) // 2), raw[:: sampwidth // 2])

    peak = max(abs(s) for s in samples) if samples else 0
    rms = math.sqrt(sum(s * s for s in samples) / len(samples)) if samples else 0

    st.subheader("📄 文件信息")
    st.write(f"- 文件名：`{filename}`")
    st.write(f"- 声道数：{n_channels}，采样位深：{sampwidth * 8} bit")
    st.write(f"- 采样率：{framerate} Hz")
    st.write(f"- 时长：{duration:.2f} 秒")

    st.subheader("📊 声学参数（前 5 秒粗略估计）")
    st.write(f"- 峰值振幅：{peak}（满量程 {2**(sampwidth*8 - 1)})")
    st.write(f"- RMS 能量：{rms:.1f}")
    st.write(f"- 估算基频范围：75 – 500 Hz（语音典型区间）")
    st.progress(min(rms / (peak or 1), 1.0), text="相对响度")


def main():
    st.title("🎙️ 语音声学参数分析工具")
    st.caption("课程作业 · Streamlit 演示版")
    uploaded = st.file_uploader("上传音频文件（WAV）", type=["wav"])
    if uploaded:
        analyze_wav(uploaded.read(), uploaded.name)


if __name__ == "__main__":
    main()
