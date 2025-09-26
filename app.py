# app.py
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Interactive Linear Regression Visualizer", layout="wide")
st.title("HW1-1: Interactive Linear Regression Visualizer")

# -----------------------------
# Sidebar 控制項
# -----------------------------
st.sidebar.header("Configuration")

# 1) 點數 N：100 ~ 1000
n_points = st.sidebar.slider("Number of data points (n)", 100, 1000, 500, step=10)

# 4) 斜率 a：-10 ~ 10
a = st.sidebar.slider("Slope a (y = a x + b + noise)", -10.0, 10.0, 2.0, 0.1)

# 3) 噪聲方差 var：0 ~ 1000
var = st.sidebar.slider("Noise Variance (var)", 0, 1000, 100, step=1)

# 新增：亂數種子輸入框
seed = st.sidebar.number_input("Random seed", min_value=0, max_value=10000, value=42, step=1)

# 新增：X 範圍可調
x_min, x_max = st.sidebar.slider("X range", -50.0, 50.0, (0.0, 10.0), step=1.0)

# 新增：離群值數量
n_outliers = st.sidebar.slider("Number of outliers to mark", 1, 20, 5, step=1)

# 固定截距 b（依需求）
b = 5.0

# -----------------------------
# 產生資料：y = a x + b + noise, noise ~ N(0, var)
# -----------------------------
np.random.seed(seed)  # reproducible
x = np.random.uniform(x_min, x_max, size=n_points)
y_true_line = a * x + b
noise = np.random.normal(loc=0.0, scale=np.sqrt(var), size=n_points)
y = y_true_line + noise

df = pd.DataFrame({"x": x, "y": y})

# -----------------------------
# 離群值（對真實直線 y = a x + b 的垂直殘差）
# -----------------------------
residuals = np.abs(y - (a * x + b))
df["residual"] = residuals
outliers = df.nlargest(n_outliers, "residual").copy()

# -----------------------------
# 繪圖（藍色散點 + 紅色直線 + 紅色圈圈離群值）
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# 藍色散點
ax.scatter(df["x"], df["y"], s=18, color="blue", alpha=0.85, label="Data (with noise)")

# 紅色真實直線（依 X 範圍畫平滑線）
xx = np.linspace(x_min, x_max, 200)
yy = a * xx + b
ax.plot(xx, yy, color="red", linewidth=2.5, label=r"True line $y=ax+b$")

# 標示離群值（紅色圈圈 + 編號）
ax.scatter(outliers["x"], outliers["y"],
           s=120, facecolors="none", edgecolors="red", linewidths=2,
           label="Outliers")

for rank, row in enumerate(outliers.itertuples(), start=1):
    ax.annotate(
        f"#{rank}", (row.x, row.y),
        textcoords="offset points", xytext=(6, 6),
        fontsize=9, color="red", fontweight="bold"
    )

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Simple Linear Regression (data from y = ax + b + noise)")
ax.legend(loc="best")
ax.grid(True, linestyle=":", alpha=0.4)

st.pyplot(fig, clear_figure=True)

# -----------------------------
# 資訊區塊
# -----------------------------
st.subheader("Parameters")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Selected slope a", f"{a:.2f}")
c2.metric("Noise variance var", f"{var:.0f}")
c3.metric("Intercept b (fixed)", f"{b:.1f}")
c4.metric("Random seed", f"{seed}")
c5.metric("Outliers marked", f"{n_outliers}")

st.subheader(f"Top-{n_outliers} Outliers (by vertical residual to y = ax + b)")
st.dataframe(outliers[["x", "y", "residual"]].round(3), use_container_width=True)

st.caption("離群值依『垂直殘差』 |y − (a x + b)| 排序。")
