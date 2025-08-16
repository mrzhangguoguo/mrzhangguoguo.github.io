🎯 目标
	•	托管：GitHub Pages（原生 Jekyll 构建）
	•	页面：主页、About、标签页(/tags、/tags/<tag>)、文章(/posts/<slug>)、播客(/episodes/<slug>)
	•	风格：现代极简、艺术感、深浅色模式
	•	“后台”：Decap CMS（/admin）——增删改查、草稿→发布（PR 工作流）、自定义 permalink、SEO 字段（canonical、og_image、jsonld）
	•	Feed：/rss.xml（博客）与 /podcast.xml（播客，带 enclosure）
	•	内容：仓库内 Markdown（frontmatter）

⸻

🗂 目录结构

.
├── _config.yml
├── Gemfile
├── _includes/
│   └── head-seo.html        # canonical/OG/JSON-LD
├── _layouts/
│   ├── default.html
│   ├── post.html
│   └── episode.html
├── _posts/                  # 文章：YYYY-MM-DD-标题.md（也可自定义 permalink）
├── _episodes/               # 播客：*.md（自定义 permalink）
├── pages/
│   ├── index.md
│   └── about.md
├── tags/
│   ├── index.html           # 标签索引
│   └── tag.html             # 单标签模板（通过静态生成）
├── podcast.xml              # 播客 RSS（自定义模板）
├── rss.xml                  # 博客 RSS（jekyll-feed 自动生成）
├── assets/                  # CSS（Tailwind 可选：生成后直接引入）
└── public/
    └── admin/               # Decap CMS（index.html + config.yml）


⸻

⚙️ Jekyll 基本配置

# _config.yml
title: Your Podcast
description: A modern minimal podcast + blog
url: https://<USER>.github.io      # 用户主页：用这个
baseurl: /<REPO>                   # 项目页才需要；用户主页留空
theme: minima                      # 先用默认主题，后续自定义样式
plugins:
  - jekyll-feed
  - jekyll-sitemap

collections:
  episodes:
    output: true
    permalink: /episodes/:slug/

# 文章链接：允许前言里自定义 permalink；否则走默认 /year/month/day/title
permalink: /posts/:slug/

# 构建时排除
exclude:
  - node_modules
  - Gemfile*
  - package*.json

Gemfile（让 Pages 使用官方白名单版本）

source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins

GitHub Pages 会自动构建，无需自配 Actions（保持默认即可）。

⸻

✍️ 内容规范（Frontmatter）

文章（_posts/）
	•	文件名建议：YYYY-MM-DD-any.md（便于排序）；URL 用 permalink 字段控制

---
title: 标题
tags: [design, life]
draft: true            # 草稿不会出现在导航/列表（由 CMS 控制合并）
slug: custom-slug      # 可选；用于默认 permalink
permalink: /posts/custom-slug/
canonical: https://example.com/posts/custom-slug
og_image: https://.../og.jpg
jsonld: |
  { "@context":"https://schema.org","@type":"BlogPosting","headline":"标题" }
published_at: 2025-08-10
layout: post
---
正文（Markdown）

播客（_episodes/）

---
title: 第 1 期：主题
tags: [podcast, interview]
draft: false
slug: ep-1
permalink: /episodes/ep-1/
audio_url: https://cdn.example.com/audio/ep1.mp3
duration_sec: 1800
canonical: https://example.com/episodes/ep-1
og_image: https://.../ep1.jpg
jsonld: |
  { "@context":"https://schema.org","@type":"PodcastEpisode","name":"第 1 期","associatedMedia":{"@type":"MediaObject","contentUrl":"https://cdn.example.com/audio/ep1.mp3"}}
published_at: 2025-08-12
layout: episode
---
Show notes（Markdown）


⸻

🧩 布局与 SEO

在 default.html 的 <head> 引入 SEO 片段

{% include head-seo.html %}

_includes/head-seo.html

{%- assign canon = page.canonical | default: site.url | append: site.baseurl | append: page.url -%}
<link rel="canonical" href="{{ canon }}"/>
{% if page.og_image %}<meta property="og:image" content="{{ page.og_image }}"/>{% endif %}
{% if page.jsonld %}
<script type="application/ld+json">
{{ page.jsonld }}
</script>
{% endif %}

_layouts/post.html（要点）

---
layout: default
---
<article class="post">
  <h1>{{ page.title }}</h1>
  <p class="meta">{{ page.published_at | date: "%Y-%m-%d" }}</p>
  <div class="content">{{ content }}</div>
  <p class="tags">
    {% for t in page.tags %}<a href="{{ site.baseurl }}/tags/{{ t | uri_escape }}/">{{ t }}</a>{% unless forloop.last %}, {% endunless %}{% endfor %}
  </p>
</article>

_layouts/episode.html（音频）

---
layout: default
---
<article class="episode">
  <h1>{{ page.title }}</h1>
  <audio controls src="{{ page.audio_url }}"></audio>
  <div class="content">{{ content }}</div>
</article>


⸻

🏷️ 标签页（无插件实现）

tags/index.html（索引所有标签：文章+播客）

---
layout: default
title: Tags
permalink: /tags/
---
<h1>Tags</h1>
<ul>
  {%- assign tag_map = "" | split: "" -%}
  {%- for p in site.posts -%}
    {%- unless p.draft -%}
      {%- for t in p.tags -%}{% assign tag_map = tag_map | push: t %}{% endfor -%}
    {%- endunless -%}
  {%- endfor -%}
  {%- for e in site.episodes -%}
    {%- unless e.draft -%}
      {%- for t in e.tags -%}{% assign tag_map = tag_map | push: t %}{% endfor -%}
    {%- endunless -%}
  {%- endfor -%}
  {%- assign uniq = tag_map | uniq | sort_natural -%}
  {%- for t in uniq -%}
    <li><a href="{{ site.baseurl }}/tags/{{ t | uri_escape }}/">{{ t }}</a></li>
  {%- endfor -%}
</ul>

为每个标签生成静态页：在仓库里预建一个极简生成脚本（可选），或手工常用标签页。最简做法：建 tags/tag.html 作为模板 + 用 “目录型 permalink”：

---
layout: default
title: Tag
permalink: /tags/:tag/
---
<h1># {{ page.tag }}</h1>

<h2>Posts</h2>
<ul>
{% for p in site.posts %}
  {% unless p.draft %}
    {% if p.tags contains page.tag %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endunless %}
{% endfor %}
</ul>

<h2>Episodes</h2>
<ul>
{% for e in site.episodes %}
  {% unless e.draft %}
    {% if e.tags contains page.tag %}
      <li><a href="{{ e.url | relative_url }}">{{ e.title }}</a></li>
    {% endif %}
  {% endunless %}
{% endfor %}
</ul>

提示：若不想写生成脚本，可把常用标签各自复制一份 tags/<tag>/index.md，在 Frontmatter 里设 tag: <tag> 并用上面的模板布局。

⸻

📰 RSS 与播客 Feed
	•	博客 RSS：jekyll-feed 插件自动生成 /feed.xml（你也可以放一个别名到 /rss.xml）
	•	播客 RSS：自定义 podcast.xml

---
layout: null
permalink: /podcast.xml
---
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>{{ site.title | xml_escape }}</title>
  <link>{{ site.url }}{{ site.baseurl }}</link>
  <description>{{ site.description | xml_escape }}</description>
  {% for e in site.episodes %}
    {% unless e.draft %}
    <item>
      <title>{{ e.title | xml_escape }}</title>
      <link>{{ site.url }}{{ site.baseurl }}{{ e.url }}</link>
      <guid>{{ site.url }}{{ site.baseurl }}{{ e.url }}</guid>
      {% if e.published_at %}<pubDate>{{ e.published_at | date_to_rfc822 }}</pubDate>{% endif %}
      {% if e.excerpt %}<description><![CDATA[{{ e.excerpt }}]]></description>{% endif %}
      <enclosure url="{{ e.audio_url }}" type="audio/mpeg" />
    </item>
    {% endunless %}
  {% endfor %}
</channel>
</rss>


⸻

🎛 Decap CMS（/admin）

public/admin/index.html

<!doctype html>
<html><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/></head>
<body><script src="https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js"></script></body></html>

public/admin/config.yml（用你的仓库替换）

backend:
  name: github
  repo: <OWNER>/<REPO>
  branch: main
  # 若需 OAuth 登录，部署 decap-cms-oauth-provider（免费层即可）
  base_url: https://<OAUTH-PROVIDER>
  auth_endpoint: /auth

publish_mode: editorial_workflow
media_folder: "assets/uploads"
public_folder: "{{site.baseurl}}/assets/uploads"

collections:
  - name: "posts"
    label: "Posts"
    folder: "_posts"
    create: true
    slug: "{{year}}-{{month}}-{{day}}-{{slug}}"
    fields:
      - {label: Title, name: title, widget: string}
      - {label: Draft, name: draft, widget: boolean, default: true}
      - {label: Tags, name: tags, widget: list, default: []}
      - {label: Published At, name: published_at, widget: datetime, required: false}
      - {label: Permalink, name: permalink, widget: string, required: false, hint: "/posts/<slug>/"}
      - {label: Canonical, name: canonical, widget: string, required: false}
      - {label: OG Image, name: og_image, widget: string, required: false}
      - {label: JSON-LD, name: jsonld, widget: text, required: false}
      - {label: Body, name: body, widget: markdown}

  - name: "episodes"
    label: "Episodes"
    folder: "_episodes"
    create: true
    slug: "{{slug}}"
    fields:
      - {label: Title, name: title, widget: string}
      - {label: Draft, name: draft, widget: boolean, default: true}
      - {label: Tags, name: tags, widget: list, default: []}
      - {label: Published At, name: published_at, widget: datetime, required: false}
      - {label: Permalink, name: permalink, widget: string, hint: "/episodes/<slug>/"}
      - {label: Audio URL, name: audio_url, widget: string}
      - {label: Duration (sec), name: duration_sec, widget: number, required: false}
      - {label: Canonical, name: canonical, widget: string, required: false}
      - {label: OG Image, name: og_image, widget: string, required: false}
      - {label: JSON-LD, name: jsonld, widget: text, required: false}
      - {label: Body, name: body, widget: markdown}


⸻

🎨 样式与深浅色
	•	直接写 CSS（或用预编译好的 Tailwind 输出的单 CSS 文件），在 default.html 引入。
	•	采用大留白、圆角、柔和阴影、可变字体；用 @media (prefers-color-scheme: dark) 适配暗色。

⸻

✅ 验收
	•	GitHub Pages 自动构建成功，主页/标签/详情可访问
	•	/feed.xml 与 /podcast.xml 可被抓取
	•	/admin 可创建/编辑内容；草稿不出现在站点，合并后即发布
	•	自定义 permalink、canonical、jsonld 生效
	•	标签页同时汇总文章与播客

⸻
