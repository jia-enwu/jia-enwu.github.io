# Jiaen Wu — academic job-market website

A single-page academic website hosted on GitHub Pages, built with Jekyll. The homepage presents the job market paper immediately after an introduction, followed by published papers (newest first), working papers (R&R first), grants, teaching, and background. PDF links open the documents directly.

The design follows the single-page organization in [Alex Hollingsworth’s job-market website guide](https://hollina.github.io/make-a-job-market-website.html) and [Jaehyun Choi’s website](https://choi-jaehyun.github.io/). The presentation is implemented locally in Jekyll rather than importing the older Hugo build system or another candidate’s content. The original AcademicPages / Minimal Mistakes license remains in `LICENSE`.

## Editing content

- `_pages/about.md`: introduction, job-market paper summary, grants, and background.
- `_publications/`: one Markdown document per paper. The homepage and research index share these records. Set `job_market_paper: true` on exactly one paper; it is featured above all other research.
- Paper fields: `title`, `authors`, `venue` (publication or review status), `category`, `excerpt`, and `paperurl`. Optional `paper_label` controls the download label. An empty `paperurl` hides the paper link; it does not create a placeholder download.
- Working papers are grouped by `review_status`: `revise_and_resubmit` first, `under_review` second, then `working_paper` or unspecified status. Update this field together with `venue` when a paper’s status changes.
- `_teaching/`: course descriptions, dates, and `term` labels.
- `files/Wu_CV.pdf` and `files/job_market_paper_jiaen_wu.pdf`: replace in place to keep incoming links working.
- `_config.yml`: contact details, search descriptions, and collection settings.
- `llms.txt`: short machine-readable research overview; keep its statuses current.

## Layout

- `_layouts/academic.html`: shared navigation, footer, metadata, and stylesheet.
- `_layouts/academic-page.html`: paper, course, CV, and other internal pages.
- `_includes/academic-*.html`: reusable research and teaching lists.
- `assets/css/academic.css`: responsive desktop and mobile styling, print rules, and keyboard focus states. No client-side JavaScript or external fonts are needed.

Existing `/publications/`, paper, teaching, and CV URLs are retained. `/research/` redirects to the research index. Production analytics load only when `JEKYLL_ENV=production`.

## Local preview

Use a current Ruby installation with Bundler:

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open the local address printed by Jekyll. To build for GitHub Pages:

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py _site
```

The checker verifies local links, section anchors, direct CV/JMP PDF links, and the presence of all research and teaching entries. Before publishing, visually review the homepage and one paper page at desktop and narrow mobile widths.
