> 考研英语一刷题追踪工具，支持多刷记录、年度统计、得分率曲线可视化。

![Static Badge](https://img.shields.io/badge/考研英语一-专用-b22222)
![Static Badge](https://img.shields.io/badge/纯HTML-零依赖-2d6a4f)
![Static Badge](https://img.shields.io/badge/本地%2F服务器-双模式-5c4a8a)

---

## ✨ 界面预览 

**💻 桌面端：做题总线与年度数据分析** 

<img width="1615" height="918" alt="桌面端-做题记录" src="https://github.com/user-attachments/assets/082563b8-9271-4513-bae2-9b7924023b35" />

<img width="1649" height="919" alt="桌面端-数据统计" src="https://github.com/user-attachments/assets/32d74ac6-56d0-488b-ba75-69648e1b2176" />

**📱 移动端：原生 App 级响应式体验**

<img width="300" alt="移动端适配界面" src="https://github.com/user-attachments/assets/11b72b80-8cbf-43d2-a63e-4f09da1af7a0" />

## 功能一览

- 📝 **做题记录**：支持阅读（Text 1–4）、完形填空、新题型、翻译、小作文、大作文
- 🔄 **多刷追踪**：同一篇文章支持 1/2/3 刷，统计页可按刷次切换对比
- 📊 **年度统计**：每年客观分/主观分拆分，得分率平滑曲线图（图例可点击筛选）
- 🗓 **热力图**：近 20 周打卡频率，GitHub 风格
- 💾 **数据备份**：一键导出/导入 JSON，本地永久留存
- 📱 **响应式**：桌面端左右分栏，移动端底部导航，全端适配

你可以直接在网页上体验交互和图表渲染效果：

👉 **[点击此处，进入考研英语追踪器 Live Demo](https://vesperloop.com/tools/kaoyan-tracker/)**
*(注：演示版为纯本地模式，你的任何点击和测试数据仅保存在当前浏览器缓存中，不会上传。)*

---

## 快速开始（本地模式，推荐）

**直接下载 `index.html`，用浏览器打开即可使用。**

数据自动保存在浏览器 `localStorage`，无需任何服务器。

下载仓库里的 `sample_data.json` 直接看效果，打开页面后点侧边栏「导入备份」即可加载演示数据（2010–2015年，含阅读多刷、主客观题混合记录）。
> ⚠️ 清除浏览器数据会丢失记录，建议定期点「导出备份」保存 JSON 文件。

---

## 进阶：自部署服务器模式（跨设备同步）

如果你有自己的服务器，可以部署 Flask 后端实现多设备数据同步。

### 所需文件

```
your-project/
├── index.html
└── server.py
```

### 启动后端

```bash
pip install flask
python server.py   # 默认监听 0.0.0.0:5060
```

访问 `http://localhost:5060` 即可使用，数据保存在同目录的 `data.json`。

### Docker 部署

```yaml
services:
  kaoyan-reading:
    image: python:3.10-slim
    working_dir: /app
    volumes:
      - ./:/app
    ports:
      - "5060:5060"
    command: sh -c "pip install flask --quiet && python server.py"
    restart: unless-stopped
```

### Nginx 反向代理（可选）

```nginx
location /kaoyan/english_reading/ {
    proxy_pass http://localhost:5060/;
    proxy_set_header Host $host;
}
```

### Cloudflare 用户注意

如果你的域名走 Cloudflare 代理，需要对该路径设置 **Cache Level: Bypass**，否则 `/load` 和 `/save` 请求会被缓存，导致多设备数据不同步。

Cloudflare → Rules → Page Rules → Create Page Rule：

```
URL：yourdomain.com/your-path/*
设置：Cache Level → Bypass
```

> 状态指示器：页面 header 右侧显示「☁️ 云端同步」或「💾 本地模式」，自动检测。

---

## 题型与分值

| 题型 | 类型 | 满分 |
|------|------|------|
| 阅读（Text 1–4）| 客观 | 40 |
| 完形填空 | 客观 | 10 |
| 新题型 | 客观 | 10 |
| 翻译 | 主观 | 10 |
| 小作文 | 主观 | 10 |
| 大作文 | 主观 | 20 |
| **总计** | | **100** |

---

## 数据格式

本地导出的 JSON 结构如下，可手动编辑或迁移：

```json
{
  "records": [
    {
      "id": "唯一ID",
      "examType": "英语一",
      "year": 2012,
      "questionType": "阅读",
      "article": "Text 1",
      "totalQuestions": 5,
      "correctQuestions": 4,
      "score": null,
      "timeMinutes": 20,
      "difficulty": "中等",
      "brush": 1,
      "notes": "备注",
      "date": "2026-05-15"
    }
  ]
}
```

---

## License

MIT — 随意使用、修改、分发。
