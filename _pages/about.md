---
layout: academic
permalink: /
title: "Jiaen Wu"
home: true
redirect_from:
  - /about/
  - /about.html
---

<section class="intro" aria-label="About Jiaen Wu">
  <div class="profile">
    <img class="portrait" src="{{ '/images/profile.png' | relative_url }}" alt="Jiaen Wu" width="172" height="172" fetchpriority="high">
    <h1 class="profile-name">Jiaen Wu</h1>
    <p class="profile-pronunciation">JIA-en, like “giant” without the “t.”</p>
    <p class="profile-role">Ph.D. Candidate in Public Affairs<br>Indiana University Bloomington</p>
    <p class="profile-links"><a href="mailto:{{ site.author.email }}">Email</a><a href="{{ site.author.googlescholar }}">Google Scholar</a></p>
  </div>
  <div class="intro-copy">
    <p class="eyebrow">On the 2026–27 academic job market</p>
    <p>I am a Ph.D. candidate at the O’Neill School of Public and Environmental Affairs, Indiana University Bloomington. My research focuses on <strong>public management</strong>, combining causal inference, machine learning, and large-scale administrative data.</p>
    <p class="research-focus">I study how organizational arrangements shape professional judgment, workforce behavior, and the allocation of public resources. Specifically, I examine how governments’ use of AI reshapes bureaucratic discretion and accountability for public decisions.</p>
    <p>I am the principal investigator of a <strong>$200,000 project</strong> funded by <a href="https://www.schmidtsciences.org/ai-at-work/">Schmidt Sciences’ AI at Work program</a>, examining how AI training and work design affect public officials’ analytical capacity.</p>
    <section class="research-interests" aria-labelledby="interests-heading">
      <h2 id="interests-heading">Research Interests</h2>
      <ul>
        <li>Public Management</li>
        <li>AI and Governance</li>
        <li>Bureaucratic Behavior</li>
        <li>Public Workforce Management</li>
      </ul>
    </section>
    <div class="intro-actions">
      <a class="button button-primary" href="{{ '/files/job_market_paper_jiaen_wu.pdf' | relative_url }}">Job Market Paper (PDF) <span aria-hidden="true">↗</span></a>
      <a class="button" href="{{ '/files/Wu_CV.pdf' | relative_url }}">CV (PDF) <span aria-hidden="true">↗</span></a>
    </div>
  </div>
</section>

{% assign jmp = site.publications | where: 'job_market_paper', true | first %}
<section class="section section-jmp" id="job-market-paper" aria-labelledby="jmp-heading">
  <div class="section-inner">
    <div class="section-heading">
      <h2 id="jmp-heading">Job Market Paper</h2>
      <p>AI, professional judgment,<br>and bureaucratic capacity</p>
    </div>
    <article class="paper-card">
      <h3 class="jmp-title"><a href="{{ jmp.paperurl | relative_url }}">{{ jmp.title }}</a></h3>
      <p class="authors">{{ jmp.authors | join: ', ' }}</p>
      <p class="publication-status">{{ jmp.venue }}</p>
      <p>I develop the concept of <em>routinized deference</em> to explain how organizational pressures can make following algorithmic advice more defensible than exercising independent judgment. Using a stacked difference-in-differences design in U.S. Child Protective Services, I find that predictive screening adoption was associated with a 15% decline in substantiation rates, longer investigations, and increasing alignment between frontline decisions and model-derived risk scores.</p>
      <p><strong>Key takeaway:</strong> AI’s contribution to bureaucratic capacity depends on how agencies incorporate it into everyday work and support professional judgment.</p>
      <div class="paper-actions">
        <a class="button button-primary" href="{{ jmp.paperurl | relative_url }}">Read paper (PDF) <span aria-hidden="true">↗</span></a>
        <a href="{{ jmp.url | relative_url }}">Research details <span aria-hidden="true">→</span></a>
      </div>
    </article>
  </div>
</section>

{% include academic-research.html home=true %}

<section class="section section-grants" id="grants" aria-labelledby="grants-heading">
  <div class="section-inner">
    <div class="section-heading">
      <h2 id="grants-heading">Grants</h2>
    </div>
    <div>
      <article class="project">
        <h3>AI at Work Grant</h3>
        <p class="publication-status">2026 · Principal investigator · US$200,000 · Schmidt Sciences</p>
        <p>Supported by <a href="https://www.schmidtsciences.org/ai-at-work/">Schmidt Sciences’ AI at Work program</a>, I am conducting a field experiment with Pakistan’s Federal Board of Revenue. The project examines how AI training and work design affect officers’ analytical capacity and whether these changes shift enforcement from small-taxpayer audits toward large-firm investigations.</p>
      </article>
      <article class="project">
        <h3>Top Grant</h3>
        <p class="publication-status">2026 · Principal investigator · US$30,000 · National Science and Technology Council (Taiwan)</p>
      </article>
    </div>
  </div>
</section>

<section class="section section-teaching" id="teaching" aria-labelledby="teaching-heading">
  <div class="section-inner">
    <div class="section-heading">
      <h2 id="teaching-heading">Teaching</h2>
      <p>Public management,<br>program evaluation,<br>and quantitative methods</p>
    </div>
    <div>
      <p>My teaching prepares future public servants to understand public organizations and make informed, accountable decisions. Through public management cases, policy simulations, and program evaluation, students weigh competing values, consider the perspectives of affected communities, and explain the reasoning behind their choices.</p>
      {% include academic-teaching.html %}
    </div>
  </div>
</section>
