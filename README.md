# NiuMaSearch-牛马搜索

本科《智能信息检索》课程设计。

## 界面预览

![搜索界面](https://github.com/Kuludu/NiuMaSearch/raw/master/img/search.png)

![结果界面](https://github.com/Kuludu/NiuMaSearch/raw/master/img/result.png)

## 目录结构说明

```
NiuMaSearch
├─ README.md
├─ app.py  # 主程序入口
├─ documents  # 文档集
│    ├─ cow.txt
│    └─ 牛马语录.txt
├─ requirements.txt
├─ searcher  # 搜索器
│    ├─ base_searcher.py  # 基搜索器（元定义）
│    ├─ bool_searcher.py  # 布尔搜索器
│    └─ phase_searcher.py  # 短语搜索器
├─ static  # 静态文件
│    └─ banner.png
├─ templates  # 前端模板
│    ├─ result.html
│    └─ search.html
└─ utils  # 工具类
     ├─ crawler.py  # 爬虫
     ├─ stop_word_loader.py  # 停用词加载器
     ├─ stop_words.txt  # 停用词
     ├─ text_loader.py  # 词库加载器
     └─ text_scorer.py  # 文档评分器
```

***

课设时间仓促，难免有差错，请谅解。