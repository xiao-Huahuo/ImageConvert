# 图片转换神器
### 基本功能
##### 主页面
- 利用PIL库,`jpg`,`jpeg`,`png`,`ico`图片格式之间的相互转换.
- 用户可选择目标图片和转换格式,系统自动检测图片格式,转换时会提示转换时的损失.
##### 菜单
- 可检测ICO文件分辨率.
### 项目结构
`utils/converter/`中存储的文件为两个格式的相互转换工具,并且文件名全为A_B.py,文件中必须要包含A->B+B->A的双向转换的两个函数,函数命名为`a_to_b(input_path,output_path)`和`b_to_a(input_path,output_path)`.
`utils/menu/`中存储的为菜单栏工具.