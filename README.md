# Aqua-Cam

摄影后处理相关的工具，适用于FujiFilm X-T30。

> 基于Streamlit和koko-learn(自开发)。

[![GitHub License](https://img.shields.io/github/license/yiyifengheju/aqua-cam)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/yiyifengheju/aqua-cam)](https://github.com/yiyifengheju/aqua-cam)
[![GitHub Forks](https://img.shields.io/github/forks/yiyifengheju/aqua-cam)](https://github.com/yiyifengheju/aqua-cam)

## 壹丨简介

Aqua-Cam 是一个基于Streamlit框架和koko-learn库开发的摄影工具，旨在提供摄影后处理功能，包括：

* RAF文件重命名
* 图片压缩WebP
* 封面压缩WebP
* 图片水印
* MkDocs文档生成及自动排版

## 贰丨安装&使用

第一步，克隆仓库到本地
```
git clone https://github.com/yiyifengheju/aqua-cam.git
```

第二步，安装`koko-learn`
```
rye add koko-learn --path path/to/koko_learn-2024.08.tar.gz
```

第三步，启动应用
```
streamlit run home.py
```


## 叁丨许可

MIT License

Copyright (c) 2024 Artmallo <wego_mao@hotmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
