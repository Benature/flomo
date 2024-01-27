<a href="https://flomoapp.com/"><img src="https://raw.githubusercontent.com/Benature/flomo/main/flomo/media/logo-192x192.png" height="100" align="right"></a>

# flomo 浮墨

[![PyPI](https://img.shields.io/pypi/v/flomo)](https://pypi.org/project/flomo/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flomo)
[![GitHub stars](https://img.shields.io/github/stars/Benature/flomo)](https://github.com/Benature/flomo)

一个非官方的 API python 玩具盒 👀

> *prefer python3.7+*  
> 欢迎 Star 🌟、Fork 🍴、Issue 💬、PR. 一起让 flomo 用的更加得心应手

最新版在 dev 分支

## Usage 使用

```shell
pip install -U flomo
```

```python
from flomo import Flomo, Parser
authorization = "Bearer xxxxxxxxxxx"
flomo = Flomo(authorization)
memos = flomo.get_all_memos()

memo = Parser(memos[-1])
print(memo.text) # memo 纯文本
print(memo.url)  # memo 链接
print(memo.tags)
```

`authorization` 是用户 flomo 登录后获取的 token，可在浏览器的开发者工具中查看。

如有疑问，欢迎 issue。

## Local Install 本地安装

```shell
git clone https://github.com/Benature/flomo.git
make all
```


## Relative Project 相关项目

- workflow: [Benature/flomo workflow](https://github.com/Benature/flomo-workflow)
- npm: [geekdada/flomo api helper](https://github.com/geekdada/flomo-api-helper)
