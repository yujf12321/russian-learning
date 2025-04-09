# 俄语阅读与翻译应用

这是一个用于学习俄语的Web应用，提供B1-B2级别的俄语文章，支持单词级别的翻译功能。

## 功能特点

- 提供B1-B2级别的俄语文章
- 支持单词级别的翻译（鼠标悬停显示）
- 左右布局，俄语原文在左，中文翻译在右
- 响应式设计，适配不同设备

## 安装说明

### 系统要求

- Python 3.8+
- Conda环境

### 安装步骤

1. 克隆或下载项目代码
2. 创建并激活Conda环境：
   ```bash
   conda create -n russian python=3.8
   conda activate russian
   ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 初始化数据文件：
   ```bash
   python init_data.py
   ```
5. 创建文章和翻译数据：
   ```bash
   python create_data_files.py
   ```

## 运行应用

1. 确保已激活Conda环境：
   ```bash
   conda activate russian
   ```
2. 运行Flask应用：
   ```bash
   python app.py
   ```
3. 在浏览器中访问：`http://localhost:5000`

## 使用说明

1. 从下拉菜单中选择想要阅读的文章
2. 文章会以左右布局显示，左侧是俄语原文，右侧是中文翻译
3. 将鼠标悬停在俄语单词上，可以看到该单词的中文翻译

## 数据文件

应用使用两个JSON文件存储数据：

- `data/articles.json`: 存储文章数据，包括标题、内容和翻译
- `data/translations.json`: 存储单词级别的翻译词典

### 文章数据格式

```json
[
  {
    "id": 1,
    "title": "文章标题",
    "content": "俄语原文",
    "translation": "中文翻译"
  }
]
```

### 翻译词典格式

```json
{
  "俄语单词": "中文翻译",
  "另一个单词": "另一个翻译"
}
```

## 技术栈

- 后端：Flask
- 前端：HTML/CSS/JavaScript
- 数据存储：JSON文件

## 注意事项

- 确保在运行应用前已正确初始化数据文件
- 如需添加新文章，可以编辑 `create_data_files.py` 文件
- 建议定期备份数据文件

## 故障排除

如果遇到问题：

1. 确保已激活正确的Conda环境
2. 检查数据文件是否正确初始化
3. 查看Flask应用的日志输出
4. 确保所有依赖包都已正确安装

## 文章内容

目前包含以下主题的文章：
- 圣彼得堡旅游
- 俄罗斯美食
- 俄罗斯民间故事
- 19世纪俄罗斯文学
- 俄罗斯节日

## 技术栈

- 后端：Flask
- 前端：HTML, CSS, JavaScript
- 模板引擎：Jinja2

## 注意事项

- 确保系统已正确安装Python和所需依赖
- 建议使用现代浏览器（Chrome、Firefox、Edge等）访问应用
- 如遇到问题，请检查控制台输出的错误信息 