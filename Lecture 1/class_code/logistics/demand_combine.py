import os
import pandas as pd

cwd = os.path.abspath("")
files = os.listdir(cwd)

print("当前工作目录:", cwd)
print("目录下文件:", files)

df = pd.DataFrame()
for file in files:
    if file.startswith("Demand") and file.endswith(".xlsx"):
        print("正在读取:", file)
        df = pd.concat([df, pd.read_excel(file)], ignore_index=True)
df.to_excel("combined_demand.xlsx", index=False)
print("合并完成，输出文件 combined_demand.xlsx")
