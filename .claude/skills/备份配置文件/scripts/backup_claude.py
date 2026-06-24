import os
import shutil
import datetime


def backup_config():
    # 1. 定义源文件路径
    source_path = "/Users/whitley/.claude.json"

    # 2. 检查源文件是否存在
    if not os.path.exists(source_path):
        return f"错误：找不到源文件 {source_path}"

    # 3. 生成时间戳 (格式：年-月-日-时-分-秒)
    # 注意：为了文件系统兼容性，建议使用数字格式 (YYYY-MM-DD-HH-MM-SS)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # 4. 构建目标文件名
    # 格式：.claude.json.myautoback-2023-10-27-10-30-05
    destination_path = f"{source_path}.myautoback-{timestamp}"

    try:
        # 5. 执行复制 (copy2 保留文件元数据)
        shutil.copy2(source_path, destination_path)
        return f"成功：配置文件已备份至 {destination_path}"
    except Exception as e:
        return f"备份失败：{str(e)}"


if __name__ == "__main__":
    result = backup_config()
    print(result)