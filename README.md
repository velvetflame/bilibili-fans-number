# B站UP主实时粉丝数

主要是设计给主播直播冲刺粉丝数用的，可搭配`obs`/`直播姬`使用

![obs截图](https://github.com/velvetflame/bilibili-fans-number/blob/main/screenshots/obs.jpg)

## 特性
* 兼容多种B站推流软件
* 实时更新up主粉丝数
* 动画滚动电子屏样式

## 使用办法
### 一.部署
1.clone仓库
```sh
git clone https://github.com/velvetflame/bilibili-fans-number
```

2.修改up uid`get_fans_number.py`
```py
API = {
    "url": "https://api.bilibili.com/x/relation/stat",
    "params": {
        "vmid": 477792 #这里改成你想要展示的up主uid
    }
}
```

3.运行
```sh
cd backend
pip install -r requirements.txt
python get_fans_number.py
```

4.修改`index.html`中的 json path
```html
ajax._url="{PATH to json}?"+Math.random(); 
//路径后加? Eg:"/data/fansnumber.json?"
```

### 二.使用
在obs中添加`浏览器源`，网址填写前端页面的地址，宽高自定（推荐400*200）
