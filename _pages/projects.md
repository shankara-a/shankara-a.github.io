---
layout: page
title: software
permalink: /projects/
description: Open-source software, algorithms, and publication code repositories I've developed for cancer genomics and computational biology.
nav: true
nav_order: 2
display_categories: ["Bioinformatics Tools", "Publication Repositories"]
horizontal: false
---

<!-- pages/projects.md -->
<style>
  .github-link-footer {
    display: block;
    background: none;
    border-top: 1px solid var(--global-divider-color);
    padding: 0.6rem 1rem;
    text-decoration: none;
    transition: background-color 0.15s ease, color 0.15s ease;
  }
  .github-link-footer:hover {
    background-color: color-mix(in srgb, var(--global-theme-color) 12%, var(--global-bg-color));
    text-decoration: none;
  }
  .github-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--global-text-color);
    transition: color 0.15s ease;
  }
  .github-link-footer:hover .github-link {
    color: var(--global-theme-color);
  }
  .github-link i.fa-github {
    font-size: 1.15rem;
  }
</style>
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
