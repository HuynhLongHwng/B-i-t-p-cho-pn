import numpy as np

num_stations = int(input("Nhập số lượng trạm quan trắc: "))
rainfall_data = np.array([[
    float(input(f"Lượng mưa trung bình tháng {month + 1} cho trạm {station + 1}: "))
    for month in range(12)] for station in range(num_stations)])

annual_rainfall = np.mean(rainfall_data, axis=1)

monthly_average = np.mean(rainfall_data, axis=0)

highest_station = np.argmax(annual_rainfall)
lowest_station = np.argmin(annual_rainfall)

print("\nLượng mưa trung bình năm cho từng trạm:")
for i, rainfall in enumerate(annual_rainfall):
    print(f"Trạm {i + 1}: {rainfall:.2f} mm")

print(f"\nTrạm có lượng mưa cao nhất là trạm {highest_station + 1}.")
print(f"Trạm có lượng mưa thấp nhất là trạm {lowest_station + 1}.")

print("\nLượng mưa trung bình từng tháng cho tất cả các trạm:")
for month, avg_rainfall in enumerate(monthly_average, start=1):
    print(f"Tháng {month}: {avg_rainfall:.2f} mm")
