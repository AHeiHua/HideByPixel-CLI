# HideByPixel-CLI
基于 [HideByPixel](https://github.com/HFO4/HideByPixel) 开发的命令行工具
通过修改像素LSB（最低有效位）实现文本信息的嵌入与提取

## 主要功能
✅ 文本嵌入：将任意文本信息隐藏到PNG图片中  
✅ 信息提取：从已嵌入信息的图片中还原原始文本  
✅ 无损处理：保证处理后图片的视觉效果基本不变  
✅ 安全标记：使用特定起始/结束标记保证数据完整性

## 环境要求
- Python 3.8+
- Pillow 10.0+
- numpy 1.26+

```bash
# 安装依赖
pip install -r requirements.
```
## 使用方法
### 文本嵌入
```bash
python main.py -e -i input.png -o output.png -m "Hello, World!"
```
### 信息提取
```bash
python main.py -d -i input.png -o output.txt
```
## 注意事项
- 确保输入图片是PNG格式，支持Alpha通道
- 文本信息长度应小于图片像素数
- 提取的文本信息可能包含起始/结束标记，需自行处理


