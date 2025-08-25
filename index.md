---
layout: default
title: Home
sitemap: 
  priority: 1.0
  changefreq: daily
---

<div class="home-wrapper">
  <!-- Hero Section - Full Width -->
<section class="hero {% if site.hero_image %}has-banner{% endif %}" {% if site.hero_image %}style="background-image: url('{{ site.hero_image | relative_url }}');"{% endif %}>
  <div class="hero-inner">
    <h1>{{ site.title }}</h1>
    <p class="hero-description">{{ site.description }}</p>
  </div>
</section>
  
  <!-- Content with Sidebar -->
  <div class="content-with-sidebar">
    <div class="home-content">

  <section class="recent-posts">
    <h2>Latest Posts</h2>
    {% assign recent_posts = site.posts | where_exp: "post", "post.draft != true" | limit: 5 %}
    {% if recent_posts.size > 0 %}
      <div class="post-list">
        {% for post in recent_posts %}
          <article class="post-card">
            <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
            <div class="post-meta">
              <time datetime="{{ post.published_at | default: post.date | date_to_xmlschema }}">
                {{ post.published_at | default: post.date | date: "%Y年%-m月%-d日" }}
              </time>
              {% if post.tags and post.tags.size > 0 %}
                <div class="tags">
                  {% for tag in post.tags limit: 3 %}
                    <span class="tag">#{{ tag }}</span>
                  {% endfor %}
                </div>
              {% endif %}
            </div>
            {% if post.excerpt %}
              <p class="post-excerpt">{{ post.excerpt | strip_html | truncate: 150 }}</p>
            {% endif %}
          </article>
        {% endfor %}
      </div>
      <a href="/posts/" class="view-all">View all posts →</a>
    {% else %}
      <p>No posts yet. <a href="/public/admin/">Create your first post</a>!</p>
    {% endif %}
  </section>

  <section class="recent-episodes">
    <h2>Latest Episodes</h2>
    {% assign recent_episodes = site.episodes | where_exp: "episode", "episode.draft != true" | limit: 3 %}
    {% if recent_episodes.size > 0 %}
      <div class="episode-list">
        {% for episode in recent_episodes %}
          <article class="episode-card">
            <h3><a href="{{ episode.url | relative_url }}">{{ episode.title }}</a></h3>
            <div class="episode-meta">
              <time datetime="{{ episode.published_at | default: episode.date | date_to_xmlschema }}">
                {{ episode.published_at | default: episode.date | date: "%Y年%-m月%-d日" }}
              </time>
              {% if episode.duration_sec %}
                <span class="duration">{{ episode.duration_sec | divided_by: 60 }} min</span>
              {% endif %}
            </div>
            {% if episode.audio_url %}
              <audio controls preload="metadata" class="episode-preview">
                <source src="{{ episode.audio_url }}" type="audio/mpeg">
              </audio>
            {% endif %}
          </article>
        {% endfor %}
      </div>
      <a href="/episodes/" class="view-all">View all episodes →</a>
    {% else %}
      <p>No episodes yet. <a href="/public/admin/">Create your first episode</a>!</p>
    {% endif %}
  </section>
    </div>
    
    <!-- Sidebar -->
    {% include home-sidebar.html %}
  </div>
</div>
