现代JavaScript库开发：原理、技术与实战
########################################################

:date: 2024-03-31 11:00
:author: Kaffa
:category: book
:tags: javascript
:slug: modern-javascript-library-development-principles-techniques-and-practice
:summary: 如果你打算定制JavaScript库，则本书不容错过。
:image: /static/img/2024/hero.png
:subject_url: https://neodb.social/book/6AArjUFpQnOXFwLs7aUHNe


评分
====================

⭐⭐⭐⭐⭐
⭐⭐⭐ 8/10


摘录
====================

2009年是前端技术分水岭，从刀耕火种到 node.js，迈入工具化时代。

模块化技术：

- 传统方式：用 function 创建作用域
- AMD：异步模块加载规范，浏览器不支持，需借助 RequireJS
- CommonJS：同步模块加载规范，node.js
- UMD：通用混合规范
- ES Module：入口文件为 index.esm.js

工具化体系：

- webpack
- rollup.js


+-------------------+-----------------------------+----------+-----------+
| 打包输出文件      | 配置文件                    | 技术体系 | 模块规范  |
+===================+=============================+==========+===========+
| dist/index.js     | config/rollup.config.js     | Node.js  | CommonJS  |
| dist/index.esm.js | config/rollup.config.esm.js | webpack  | ES Module |
| dist/index.aio.js | config/rollup.config.aio.js | 浏览器   | UMD       |
+-------------------+-----------------------------+----------+-----------+


