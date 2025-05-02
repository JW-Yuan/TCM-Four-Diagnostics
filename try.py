import numpy as np
import matplotlib.pyplot as plt

fs = 50  # 采样频率
duration = 5  # 秒
t = np.linspace(0, duration, fs * duration)

# 基础心率频率为 75bpm = 1.25Hz
heart_rate = 1.25  # Hz
base_wave = 0.3 * np.sin(2 * np.pi * heart_rate * t)

# 添加浮脉特征：尖锐的波峰，使用高斯分布模拟
pulse_wave = np.zeros_like(t)
for beat_time in np.arange(0, duration, 1 / heart_rate):
    pulse_wave += np.exp(-((t - beat_time) ** 2) / (2 * (0.05 ** 2)))

# 合成波形
synthetic_pulse = base_wave + pulse_wave

# 归一化
normalized_pulse = (synthetic_pulse - np.min(synthetic_pulse)) / (np.max(synthetic_pulse) - np.min(synthetic_pulse))

# 绘图
plt.figure(figsize=(10, 3))
plt.plot(t, normalized_pulse)
plt.title("模拟浮脉波形（归一化） - 50Hz, 5秒")
plt.xlabel("时间 (秒)")
plt.ylabel("归一化幅值")
plt.grid(True)
plt.tight_layout()
plt.show()
