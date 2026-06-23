---
layout: about
title: about
permalink: /
subtitle: Hematology/Oncology Fellow, Stanford Health Care

profile:
  align: left
  image: prof_pic.jpg
  image_circular: true # crops the image to make it circular
  title: Hematology/Oncology Fellow
  location: Stanford, CA

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

<style>
  .about-layout {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    gap: 2.5rem;
  }

  .about-sidebar {
    flex: 0 0 220px;
    width: 220px;
    max-width: 220px;
    text-align: center;
    position: sticky;
    top: 1.5rem;
    align-self: flex-start;
  }

  .about-sidebar .about-photo {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    margin-bottom: 1rem;
  }

  .about-name {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
  }

  .about-title,
  .about-location {
    font-size: 0.95rem;
    margin: 0.15rem 0;
    color: var(--global-text-color-light);
  }

  .about-social {
    margin-top: 1rem;
  }

  .about-social .contact-icons {
    font-size: 1.5rem;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.85rem;
  }

  .about-social .contact-icons a img,
  .about-social .contact-icons a svg {
    width: 1.5rem;
    height: 1.5rem;
    margin-bottom: 0;
  }

  .about-main {
    flex: 1 1 320px;
    min-width: 0;
    text-align: left;
  }

  .about-main h2 {
    margin-top: 2.5rem;
  }

  .about-main h2:first-child {
    margin-top: 0;
  }

  .about-main .publications .row {
    margin-left: 0;
    margin-right: 0;
  }

  .about-main .publications .row > .col-sm-10 {
    flex: 0 0 100%;
    max-width: 100%;
    padding-left: 0;
    padding-right: 0;
  }

  @media (max-width: 768px) {
    .about-sidebar {
      position: static;
      width: 100%;
      max-width: 320px;
      margin: 0 auto;
    }
  }
</style>

I am a Hematology/Oncology Fellow & Physician-Scientist at Stanford in the [Translational Investigator Pathway](https://im.stanford.edu/education/residency-programs/translational-research/hematology-oncology.html).

My research is at the intersection of hematology/oncology and computational 'omics. I am interested in **plasma cell dyscrasias**, **amyloidosis**, **precision oncology**, and how large datasets can be used for risk stratification, treatment decisions, and drug discovery to improve patient outcomes.

Before medical school, I spent five years as a computational biologist at the **Broad Institute of MIT & Harvard**, working with Dr. Gad Getz's lab and the [GTEx Consortium](https://gtexportal.org/). Select projects include co-leading a pan-cancer proteogenomics flagship study with the [CPTAC Consortium](https://www.cell.com/consortium/cptac), a single-nucleus, cross-tissue transcriptomic atlas of the human body with the [GTEx Consortium](https://gtexportal.org/), and genomic risk stratification of smoldering multiple myeloma.

Methodologically, my work spans **single-cell genomics, multi-omics integration, structural proteomics, and algorithm development**. My tools / repositories are available [here](/projects/), my publications are available [here](/publications/), and my training is further detailed [here](/cv/).
