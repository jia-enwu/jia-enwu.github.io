---
title: "How Generative AI Impacts Job Satisfaction: Evidence from the U.S. Federal Government"
collection: publications
authors:
  - "Jiaen Wu"
  - "Amanda Rutherford"
date: 2025-01-01
venue: "Working paper"
category: working_papers
paperurl:
excerpt: "A continuous difference-in-differences study of 25 U.S. federal agencies, showing that GenAI augmentation—not automation—is negatively associated with employee job satisfaction as work shifts from creation to verification."
---

## Overview

Generative AI is spreading quickly through the U.S. federal government, and much of the enthusiasm rests on a single promise: that these tools will lift routine administrative burdens and free public servants to spend more time on mission-critical work. Less attention has been given to what sustained interaction with GenAI does to the people using it. We argue that the effect on job satisfaction depends on how the technology is integrated—through automation, which substitutes for routine tasks, or through augmentation, which inserts model outputs into more complex human decisions. We examine a panel of 25 U.S. civilian federal agencies from 2017 to 2024, combining task-level GenAI scores from Claude usage data (Handa et al., 2025) with agency job satisfaction from the Federal Employee Viewpoint Survey, and we treat the public release of GenAI in late 2022 as an exogenous shock within a continuous difference-in-differences design. We find that automation exposure has no significant effect on job satisfaction, while augmentation exposure is negatively associated with it. The pattern is consistent with the idea that augmentation shifts public sector work from creation to verification—employees must monitor, interpret, and remain accountable for probabilistic outputs—and that this verification burden carries real psychosocial costs.

## Research Design

- **Setting:** 25 U.S. civilian federal agencies, 2017–2024 (military-affiliated organizations excluded due to national security restrictions)
- **Data:**
  - **Job satisfaction:** Federal Employee Viewpoint Survey (FEVS) global satisfaction item, aggregated to agency-year with weighted means
  - **GenAI exposure:** Anthropic Economic Index, derived from large-scale Claude usage logs, classified into *automation* vs. *augmentation* following Handa et al. (2025) and mapped onto each agency's occupational composition
- **Empirical strategy:**
  - Continuous difference-in-differences using the late-2022 public release of GenAI as an exogenous shock
  - Event-study estimates of automation and augmentation exposure
  - Leave-one-out re-estimation across the 25 agencies as a robustness check

## Key Findings

### 1. **Automation exposure has no effect on job satisfaction**
- Post-treatment event-study estimates are statistically insignificant.
- A significant pre-trend suggests routine-heavy agencies were already shifting under earlier waves of workplace technology, so GenAI automation adds little distinct marginal impact in the short term.

### 2. **Augmentation exposure lowers job satisfaction**
- Satisfaction declines significantly in the first year after adoption (point estimate = −0.907, SE = 0.26) and intensifies the next year (−1.170, SE = 0.42), a roughly 30% increase in magnitude.
- A one-standard-deviation difference in augmentation exposure corresponds to about 30% of the sample mean (3.811).

### 3. **The augmentation result is robust**
- Clean pre-trends support the parallel-trends assumption.
- Leave-one-out estimates stay negative across nearly all subsamples; significance softens only when the Department of the Treasury is excluded, and the sign never changes.

### Overall mechanism: from creation to verification
Augmentation shifts work from producing to auditing—employees prompt, check, and remain accountable for probabilistic outputs. This imposes verification burden, accountability ambiguity, and reduced task meaning, costs that automation does not carry and that efficiency-centered assessments tend to overlook.

## Results

### Figure 1. Event-Study: Automation Exposure

![Event-study estimates for automation exposure and job satisfaction](/images/genai_jobsat_fig1_automation.png)

Treatment intensity is each agency's 2017–2022 average automation exposure; the outcome is the agency-year FEVS job satisfaction score, with agency and year fixed effects and coefficients shown relative to 2022. Post-treatment estimates are statistically insignificant, while a significant pre-trend points to historical shifts already underway in these routine-heavy agencies.

### Figure 2. Event-Study: Augmentation Exposure

![Event-study estimates for augmentation exposure and job satisfaction](/images/genai_jobsat_fig2_augmentation.png)

Using the same specification with 2017–2022 average augmentation exposure as the treatment intensity, the pre-treatment coefficients are indistinguishable from zero, supporting parallel trends. Following the 2022 release of GenAI, augmentation exposure is associated with a statistically significant decline in job satisfaction that deepens the next year.
