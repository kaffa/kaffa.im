# AGENTS.md

本文件定义 AI 助手在本项目（Kaffa.im 个人网站）中协作时必须遵守的规则。

## 规则 1：AI 工作区隔离（docs.ai）

- 本项目约定 `docs.ai/` 为 AI 专用工作目录。
- `docs.ai/` 已在 `.gitignore` 中忽略，其中的文件不会被提交到 Git 仓库。
- **未经用户明确允许，AI 的所有交互产物与测试内容只能写入 `docs.ai/` 目录**，包括但不限于：
  - 临时脚本、测试代码
  - 验证用的中间产物、日志、输出文件
  - 草稿、实验性内容
- 需要写入 `docs.ai/` 以外的目录（例如修改 `content/`、`theme/`、`plugins/`、根目录配置等正式文件）时，必须先征得用户允许。
- `docs.ai/` 仅用于本地探索与验证，不作为站点正式内容的来源。

## 规则 2：代码修改规范

修改本项目代码时，**以项目现有风格为准，不做风格重构**。新增代码应与周边代码读起来一致。

### 2.1 Python 风格

- 遵循 PEP 8，**4 空格缩进**，不使用 Tab。
- 文件首部保留编码声明：`# -*- coding: utf-8 -*-`；`pelicanconf.py` 一类需要兼容的入口文件保留 `#!/usr/bin/env python` 与 `from __future__ import unicode_literals`。
- 源码一律 **UTF-8 无 BOM** 编码。
- 命名沿用现状：类名 `PascalCase`（`Project`、`Friend`），函数与变量 `snake_case`（`get_list`、`cover_image_path`），配置常量 `UPPER_SNAKE_CASE`（`MENUITEMS`、`CATEGORY_DICT`、`KAFFAPOD`）。
- 导入顺序：标准库 → 第三方库 → 项目本地模块，各组之间空一行；需要跨目录导入本地模块时沿用 `sys.path.append(os.curdir)` 的既有做法。
- 可执行脚本保留「模块级 `get_list()` 提供数据 + `if __name__ == '__main__': main()` 便于单独调试」的结构（参考 `projects.py`、`comments.py`、`friends.py`）。
- 现有脚本**不使用类型注解、不使用 f-string 之外的格式化技巧**；不要为新代码擅自引入类型注解或改动函数签名，避免与模板层调用方式冲突。**本条持续生效，直到 Python 运行环境升级后要求必须编写类型注解时为止**；届时需先同步修订本条与 2.1 相关描述，再在代码中引入。
- SQL 使用三引号多行字符串书写，保持缩进对齐（参考 `projects.py` 中的统计 SQL）。
- Pelican 插件须实现 `register()` 并通过 `pelican.signals` 连接信号，函数不抛未捕获异常（参考 `kaffapod.py`、`followclaim.py`）。

### 2.2 注释约定

- **注释使用中文**，与现有代码保持一致。
- 修改配置或公共逻辑时，沿用「日期 + 动作」的行内变更注释格式：

  ```python
  # 20230913 添加
  # 20231019 修改
  ```

  日期取当天，动作词只用`添加`/`修改`/`删除`/`废弃`。
- 配置块使用简短分区标题注释，如 `# plugin: sitemap`、`# My Data`、`# menu`。
- 注释解释「为什么这么做」而不是复述代码。不要删除已有的日期变更注释。
- 遗留的调试用文件日志（如插件里的 `logging.FileHandler('d:/app.log')`）属于既有行为，**未经授权不要一并清理**，以免连带影响其他排查习惯。

### 2.3 内容文件约定

- 文件名格式：`YYYYMMDD-标题.rst` 或 `YYYYMMDD-标题.md`，日期为该文件创作日期，允许标题含中文。
- 文件必须落在 `content/` 下带序号的分类目录中（如 `content/2.笔记/3.数智/`）。
- RST 头部为「标题 + `#` 下划线」，随后是元数据字段列表：

  ```rst
  :date: 2026-04-06 22:55
  :author: Kaffa
  :category: reading
  :tags: Rubik Cube
  :slug: play-rubik-cube
  :summary: 本文记录了，我玩魔方的事。
  ```

- `:category:` 取值必须是 `pelicanconf.py` 中 `CATEGORY_DICT` 已定义的 slug；章节标题下级用 `=`，再下级用 `-`。
- 书影音类条目额外使用 `:image:` 与 `:subject_url:`（供 `kaffapod` 插件抓取）。
- **不要改动 `docs/` 目录**，它是构建产物，由 Pelican 生成。

### 2.4 提交信息格式

- 本项目历史提交信息统一为 `Kaffa`（由 `aio.cmd`、`tools/commit.cmd` 中的 `git commit -am 'Kaffa'` 产生）。
- **AI 不得自行提交或推送**，仅在用户明确要求时执行；不得擅自改变上述既有提交信息格式。
- 当用户明确要求撰写有意义的提交信息时，采用约定式前缀 + 中文描述：

  ```
  <type>: <简短中文描述>

  type 取值：feat / fix / content / theme / plugin / chore
  示例：plugin: kaffapod 增加封面下载失败时的降级处理
  ```

- 一次提交只包含一个主题；`git add .` 之前先确认工作区无意外改动，绝不把 `docs.ai/`、`.env`、`dbconfig.py` 等已忽略或敏感文件加入暂存区。

### 2.5 安全与可移植性

- 新增配置项、密钥、令牌一律走 `.env`（参考 `comments.py` 使用 `load_dotenv()` 读取 `GHP_ACCESS_TOKEN`），不得硬编码口令；`dbconfig.py` 已被忽略，不要将其纳入版本控制。
- 避免新增硬编码绝对路径（如 `D:/...`、`d:/app.log`）；确需时使用 `pelicanconf.py` 中的配置项或 `os.path` 派生，而非写死在模块内。

## 版本记录

- **2.0**（tag：`kaffa.im-2.0`）：规则基线版本。包含规则 1（AI 工作区隔离 `docs.ai/`）与规则 2（代码修改规范）；同时确立 `AGENTS.md`、`.gitignore` 与当前站点源码的完整基线快照。
- **3.0 起**：后续与 AI 对话产生的更新均从 3.0 开始计版，每次引入新规则或修改既有规则时，在本节追加一条版本号与变更摘要。
