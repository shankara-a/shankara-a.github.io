---
layout: page
permalink: /publications/
title: publications
description: Peer-reviewed publications, preprints, and book chapters, in reverse chronological order.
nav: true
nav_order: 1
---

<!-- _pages/publications.md -->

{% if site.data.citations.metadata.last_updated %}
  <div class="scholar-stats" style="display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.5rem;">
    <a
      href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}&hl=en"
      target="_blank"
      rel="noopener"
      style="flex: 1 1 120px; text-align: center; padding: 0.75rem 1rem; border: 1px solid var(--global-divider-color); border-radius: 8px; text-decoration: none; color: inherit;"
    >
      <div style="font-size: 1.75rem; font-weight: 700;">{{ site.data.citations.metadata.citedby }}</div>
      <div style="font-size: 0.85rem; opacity: 0.7;">Total Citations</div>
    </a>
    <a
      href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}&hl=en"
      target="_blank"
      rel="noopener"
      style="flex: 1 1 120px; text-align: center; padding: 0.75rem 1rem; border: 1px solid var(--global-divider-color); border-radius: 8px; text-decoration: none; color: inherit;"
    >
      <div style="font-size: 1.75rem; font-weight: 700;">{{ site.data.citations.metadata.hindex }}</div>
      <div style="font-size: 0.85rem; opacity: 0.7;">h-index</div>
    </a>
    <a
      href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}&hl=en"
      target="_blank"
      rel="noopener"
      style="flex: 1 1 120px; text-align: center; padding: 0.75rem 1rem; border: 1px solid var(--global-divider-color); border-radius: 8px; text-decoration: none; color: inherit;"
    >
      <div style="font-size: 1.75rem; font-weight: 700;">{{ site.data.citations.metadata.i10index }}</div>
      <div style="font-size: 0.85rem; opacity: 0.7;">i10-index</div>
    </a>
    <a
      href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}&hl=en"
      target="_blank"
      rel="noopener"
      style="flex: 1 1 120px; text-align: center; padding: 0.75rem 1rem; border: 1px solid var(--global-divider-color); border-radius: 8px; text-decoration: none; color: inherit;"
    >
      <div style="font-size: 1.75rem; font-weight: 700;">{{ site.data.citations.metadata.num_publications }}</div>
      <div style="font-size: 0.85rem; opacity: 0.7;">Publications</div>
    </a>
  </div>
  <p style="font-size: 0.8rem; opacity: 0.6; margin-top: -1rem; margin-bottom: 1.5rem;">
    Stats from <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}&hl=en" target="_blank" rel="noopener">Google Scholar</a>,
    last updated {{ site.data.citations.metadata.last_updated }}.
  </p>
{% endif %}

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>
