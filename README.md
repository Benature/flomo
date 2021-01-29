<a href="https://flomoapp.com/"><img src="https://raw.githubusercontent.com/Benature/flomo/main/flomo/media/logo-192x192.png" height="100" align="right"></a>

# flomo 浮墨

[![PyPI](https://img.shields.io/pypi/v/flomo)](https://pypi.org/project/flomo/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flomo)
[![GitHub stars](https://img.shields.io/github/stars/Benature/flomo)](https://github.com/Benature/flomo)

一个非官方的 API python 玩具盒  （包括支持官方 API） 👀

> *prefer python3.7+*  
> 欢迎 Star 🌟、Fork 🍴、Issue 💬、PR. 一起让 flomo 用的更加得心应手

最新版在 dev 分支

## Usage 使用

```shell
pip install -U flomo
```

```python
import flomo
client = flomo.Flomo(api='https://flomoapp.com/xxxxxAPIxxxx')
client.new('hello flomo')
```

相关 workflow 示例可参考 [flomo workflow](https://github.com/Benature/flomo-workflow)

```python
def get(self, tag=''):
    '''get all memo'''

def update(self, slug, content, file_ids=[], parent_memo_slug=None, source='web'):
    '''update a memo'''

def new(self, content, parent_memo_id=None, file_ids=[], source='web', method='api'):
    '''put a new memo
    @content: memo content
    @method: `api` or `cookies`, determine the method to send the new memo
    return response'''
```


## Relative Project 相关项目

- workflow: [Benature/flomo workflow](https://github.com/Benature/flomo-workflow)
- npm: [geekdada/flomo api helper](https://github.com/geekdada/flomo-api-helper)
