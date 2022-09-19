# playwright-pro

> 基于 playwright 和 pytest 单元测试框架的自动化项目

### 特点

* 测试用例运行`失败/错误`自动截图+重跑。
* 测试数据参数化。

### 安装

```shell
$ pip install -r requirements.txt
```

依赖库
```
playwright==1.25.2
pytest==7.1.2
pytest-playwright==0.3.0
pytest-html==3.1.1
pytest-rerunfailures==9.1.1
seldom==2.10.7
```

注：安装```requirements.txt```指定依赖库的版本，这是经过测试的，有时候新的版本可会有错。

### 配置

在 `config.py` 文件配置

```python
class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = "./test_dir/test_parametrize.py"

    # 配置浏览器驱动类型(chromium, firefox, webkit)。
    browser = "chromium"

    # 运行模式（True/False）
    headless = True

    # 配置运行的 URL
    url = "https://www.baidu.com"

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "5"
```

### 运行

运行测试

```shell
$ python run.py
```
