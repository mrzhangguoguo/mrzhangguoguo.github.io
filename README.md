# Jekyll Blog & Podcast Platform

A modern, minimal blog and podcast platform built with Jekyll and deployable to GitHub Pages.

## Features

- 🎨 **Modern Design** - Clean, minimal aesthetic with dark/light mode
- 📝 **Dual Content** - Support for both blog posts and podcast episodes
- 🔧 **Easy Management** - Decap CMS for content creation and editing
- 📱 **Responsive** - Perfect on all devices
- 🔍 **SEO Optimized** - Built-in meta tags, Open Graph, JSON-LD
- 🏷️ **Tagging System** - Organize content with tags
- 📡 **RSS Feeds** - Separate feeds for blog and podcast
- ⚡ **Fast & Secure** - Static site generation with GitHub Pages

## Quick Start

### 1. Setup Repository
1. Fork or clone this repository
2. Update `_config.yml` with your site details
3. Update `public/admin/config.yml` with your repository info

### 2. Deploy to GitHub Pages
1. Go to your repository settings
2. Enable GitHub Pages from the main branch
3. Your site will be available at `https://username.github.io/repository-name`

### 3. Content Management
1. Visit `/public/admin/` on your deployed site
2. Authenticate with GitHub
3. Start creating content!

## Configuration

### Site Settings (`_config.yml`)
```yaml
title: Your Site Title
description: Your site description
url: https://username.github.io
baseurl: /repository-name  # Leave empty for user pages
```

### CMS Settings (`public/admin/config.yml`)
```yaml
backend:
  name: github
  repo: username/repository-name
  branch: main
```

## Content Structure

### Blog Posts (`_posts/`)
- Filename: `YYYY-MM-DD-title.md`
- Custom permalinks supported
- SEO fields (canonical, og_image, jsonld)
- Draft/publish workflow

### Podcast Episodes (`_episodes/`)
- Audio URL and duration
- Show notes in Markdown
- Same SEO features as posts
- iTunes-compatible RSS feed

## Customization

### Styling
Edit `assets/css/style.css` to customize the design. The CSS uses custom properties for easy theming.

### Layouts
- `_layouts/default.html` - Base template
- `_layouts/post.html` - Blog post template  
- `_layouts/episode.html` - Podcast episode template

### Navigation
Edit `_includes/navigation.html` to modify the site navigation.

## Development

### Local Development
```bash
bundle install
bundle exec jekyll serve
```

### File Structure
```
.
├── _config.yml           # Jekyll configuration
├── _includes/            # Reusable template parts
├── _layouts/             # Page templates
├── _posts/               # Blog posts
├── _episodes/            # Podcast episodes
├── assets/css/           # Stylesheets
├── pages/                # Static pages
├── tags/                 # Tag archive pages
├── public/admin/         # Decap CMS
├── podcast.xml           # Podcast RSS feed
└── rss.xml              # Blog RSS feed
```

## Deployment

### GitHub Pages (Recommended)
1. Push to your repository
2. GitHub automatically builds and deploys
3. No additional configuration needed

### Manual Deployment
```bash
bundle exec jekyll build
# Upload _site/ contents to your web server
```

## Content Management

### Via CMS (Recommended)
1. Visit `/public/admin/`
2. Create/edit posts and episodes
3. Use editorial workflow for drafts

### Via Git (Advanced)
1. Create Markdown files in `_posts/` or `_episodes/`
2. Include proper front matter
3. Commit and push to deploy

## SEO Features

- Automatic meta tags
- Open Graph support
- Twitter Card support
- Custom canonical URLs
- JSON-LD structured data
- XML sitemaps
- RSS feeds

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers
- Graceful degradation for older browsers

## License

MIT License - feel free to use for personal or commercial projects.

## Support

- Check the [Jekyll documentation](https://jekyllrb.com/docs/)
- Review [GitHub Pages docs](https://docs.github.com/en/pages)
- Read [Decap CMS documentation](https://decapcms.org/docs/)

---

**Happy blogging and podcasting!** 🎉