# Project Plan for HW1-1: Linear Regression with Streamlit

## HW1-1: Interactive Linear Regression Visualizer

### Features:
1.  **Data Generation:**
    -   Generate `n` data points (x, y) where `n` is a user-selectable value between 100 and 1000.
    -   The relationship between x and y will be defined by `y = ax + b + noise`.
    -   `a`: User-selectable coefficient between -10 and 10.
    -   `noise`: Normally distributed noise `N(0, var)`, where `var` (variance) is user-selectable between 0 and 1000.

2.  **Linear Regression Visualization:**
    -   Plot the generated data points.
    -   Draw the calculated linear regression line in **red**.

3.  **Outlier Identification:**
    -   Identify and label the top 5 outliers (points furthest from the regression line).

4.  **User Interface:**
    -   Implement the application using **Streamlit** for an interactive web interface.
    -   Allow users to adjust parameters (`n`, `a`, `var`) via sliders or input fields.
    -   Display the generated plot and regression results.


prompt：
1.可讓使用者利用滑桿選擇100~1000的數字並在X-Y統計圖上產生對應數量的隨機點，點的顏色用藍色表示) 

2.根據產生的點劃出簡單線性回歸直線y=ax+b+noise。（直線顏色用紅色表示）

3.noise：常態分佈噪聲N(0, var)，其中var（方差）可由使用者在 0 到 1000 之間選擇。

4.可讓使用者利用滑桿選擇-10~10的數字調整簡單線性回歸直線y=ax+b+noise的a。

5.辨識並標示前5個離群值(離回歸直線最遠的點)

6.幫我加上亂數種子輸入框或X範圍可調

7.幫我加上離群值數量滑桿並將離群值用不同顏色標示（例如紅色圈圈）
