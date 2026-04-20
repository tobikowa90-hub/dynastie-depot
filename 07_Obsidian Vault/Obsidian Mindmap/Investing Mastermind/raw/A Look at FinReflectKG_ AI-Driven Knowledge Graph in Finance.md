---
title: "A Look at FinReflectKG: AI-Driven Knowledge Graph in Finance"
source: "https://pub.towardsai.net/a-look-at-finreflectkg-ai-driven-knowledge-graph-in-finance-d588d250948b"
author:
  - "[[Marcelo Labre]]"
published: 2025-09-29
created: 2026-04-20
description: "A Look at FinReflectKG: AI-Driven Knowledge Graph in Finance The next frontier in truth grounded on symbolic reasoning in finance Last week at the Quant x AI event here in New York, I had the …"
tags:
  - "clippings"
---
## The next frontier in truth grounded on symbolic reasoning in finance

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4MDb_1O6TuPbCnoXQK9cuQ.png)

Last week at the [Quant x AI](https://luma.com/t11yzbaw?tk=tPdvKu) event here in New York, I had the pleasure of seeing

[Fabrizio Dimino](https://medium.com/u/d22c73975ddb?source=post_page---user_mention--d588d250948b---------------------------------------)

present a compelling paper he co-authored: “ [FinReflectKG: Agentic Construction and Evaluation of Financial Knowledge Graphs](https://arxiv.org/abs/2508.17906).”

The paper tackles a critical challenge holding back financial AI. While we have powerful language models, they lack the structured, reliable symbolic reasoning systems needed to truly understand the complex world of finance. More specifically, building knowledge graphs (KGs) on regulatory documents like SEC filings is a massive hurdle.

The FinReflectKG paper offers a powerful solution with two key contributions: a new, open-source financial KG dataset and a novel framework for building it.

Here, I’ll summarize their brilliant approach and then propose a way to improving their monitoring for global semantic diversity in the model.

### The Core Innovation: A “Self-Reflecting” AI Agent

The centerpiece of the paper’s methodology is a sophisticated, three-mode pipeline for extracting knowledge “triples” (like `(Nvidia, Produces, GPUs)`) from financial documents.

While they test simpler Single-Pass and Multi-Pass methods, their most innovative approach is the Reflection-driven agentic workflow.

This agentic process works like a team:

- An Extraction LLM first takes a chunk of a document and extracts an initial set of knowledge triples.
- A Critic LLM then reviews these triples, providing structured feedback on any issues it finds, such as ambiguous entities (e.g., using “We” instead of the company ticker) or non-standard relationship types.
- A Correction LLM takes this feedback and refines the triples.

This feedback loop repeats until no more issues are found or a maximum number of steps is reached, systematically improving the quality of the extracted knowledge.

### Proving Its Worth Without a Ground Truth

A major challenge in KG construction is evaluation, as there’s often no perfect “answer key” to compare against. The authors developed a holistic evaluation framework to address this, using several complementary methods:

- CheckRules: A set of custom, rule-based checks to enforce quality and consistency. For example, rules automatically flag ambiguous subjects like “we” or “the company” and ensure all extracted entities and relationships comply with a predefined schema.
- Coverage Ratios: Metrics to measure how comprehensively the KG captures the diversity of entities and relationships present in the source documents.
- Semantic Diversity: An analysis using information theory (Shannon and Rényi entropy) to measure the balance and variety of the extracted knowledge, ensuring the graph isn’t overly skewed towards a few common concepts.
- LLM-as-a-Judge: A comparative evaluation where a powerful LLM assesses the outputs of the three different extraction modes (single-pass, multi-pass, and reflection) across four key dimensions: Precision, Faithfulness, Comprehensiveness, and Relevance.

### Key Findings and Verdict

The results clearly demonstrate the superiority of the reflection-agent mode. It consistently achieves the best balance of reliability and coverage.

- It achieved the highest compliance score, passing 64.8% of all four strict CheckRules.
- It extracted the most triples per document chunk (15.8) and had significantly higher entity and relationship coverage ratios than the other methods.
- In the LLM-as-a-Judge evaluation, it was the clear winner in Precision, Comprehensiveness, and Relevance.

The primary trade-off is speed. The iterative feedback loop requires more computation, making it less suitable for real-time applications where a single-pass approach might be preferred.

### Future Directions

The authors conclude by outlining their plans to significantly expand the project, including:

- Enlarging the dataset to cover all S&P 500 companies over the last 10 years.
- Developing a schema-free pipeline that can create ontologies from scratch, inspired by the “Extract-Define-Canonicalize” (EDC) framework.
- Building Temporal Knowledge Graphs to capture the evolution of financial relationships over time, enabling causal reasoning for applications like thematic investing.

### Suggestion: Monitoring Semantic Refinement via Cross-Entropy

The paper notes that the Reflection method, while improving compliance and coverage, reduces the diversity of the extracted elements as measured by absolute entropy. This is an expected outcome of a rule-constrained process. However, the authors’ proposal to monitor “when diversity falls below a predefined threshold” using absolute entropy presents a practical challenge: absolute entropy values are difficult to interpret and make thresholding arbitrary.

A more principled approach is to measure the relative change in the information landscape between the baseline and the refined output. I suggest a direct application of the Principle of Minimum Cross-Entropy (MinXEnt), an extension of [Jaynes’ Maximum Entropy Principle (MaxEnt)](https://link.springer.com/chapter/10.1007/978-94-009-0683-9_29). In this case, we treat the distribution from the Single-Pass method as the prior and measure how the Reflection method’s distribution diverges from it at each step.

The ideal tool for this is cross-entropy, specifically the [Kullback–Leibler (KL) Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence), which quantifies the information gain or loss when one probability distribution is used to approximate another.

### Proposed Methodology

The goal is to monitor the KL Divergence at each iteration *t* of the Reflection agent's refinement loop.

## Get Marcelo Labre’s stories in your inbox

Join Medium for free to get updates from this writer.

**1\. Establish the Prior Distribution (*p*):** First, run the Single Pass method across the corpus. From the full set of extracted elements (entities, types, and relationships), derive a normalized frequency distribution:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*yAnw9llGJrj0i6guELs1HQ.png)

This represents our baseline or *prior* understanding of the data’s structure.

**2\. Calculate Iterative Distributions (*q(t)*):** For the Reflection method, at each step *t* of the iterative feedback loop for a given chunk of text *c*, derive the corresponding normalized frequency distribution:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*SpmeZ5TQVATtvSZtr6Secw.png)

where

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ro7scJLmY6JtVnqdgSD-aw.png)

and *m* is the stopping iteration for chunk *c* as per the stopping criteria in section 4.3.3.

**3\. Unify and Smooth:** As the set of extracted elements will differ between the two methods for every *t*, a direct comparison is not possible. To solve this:

- Create a **unified vocabulary** that is the union of all unique elements found in both *p* and all *q(t)*.
- Represent all distributions over this unified vocabulary. Any element not present in a given distribution will have an initial frequency of zero.
- Apply **Laplace (add-one) smoothing** to all frequencies. This is critical to avoid zero probabilities in the denominator of the KL Divergence formula, ensuring the metric is always well-defined.

For instance, in a 5 element example we may end up with the following frequencies:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*amG7xDC0qaWBTWfmyIoM9g.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8thCcz5VB1cRER2swpR9SA.png)

In this case we have the frequency probabilities:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*6axTcGTbMAvkCTJPtU22Hw.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*rcSoLvcxmNAtPQNpmY0jiA.png)

by applying Laplace smoothing:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*hjgmqjDvS__5YYD_ndUvgg.png)

where:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*o-dpYgd4Xvj6QsHvHBfhCw.png)

![](https://miro.medium.com/v2/resize:fit:1226/format:webp/1*ULQhTgPNywIRoey6J09euw.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ggWn2kSb7hyixyjwWlQPzQ.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*JrmmaJHeVS4go2rAI_Idmg.png)

**4\. Compute KL Divergence:** For each iteration *t*, compute the KL Divergence of the Reflection distribution *q(t)* from the Single-Pass prior *p*:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*AbnjTkom2mXJple7l587Xg.png)

### Interpretation and Monitoring

By plotting *KL(q(t)|p)* against each iteration step *t*, we can directly observe the refinement process. We would expect to see the KL divergence at some point to reach a minimum. This minimum represents the *optimal point of refinement*, the iteration at which the agent has extracted the most new information without beginning to overfit or degrade the quality of the graph.

This provides a principled, data-driven stopping criterion and a far more interpretable measure of the agent’s progress than absolute entropy. More reliable monitoring thresholds can also be derived.

### The Next Frontier

The work in FinReflectKG is more than just academic exercises. It represents the blueprint for the next generation of AI. It shows us how to guide these emergent powerful models from being fluent statistical parrots toward becoming disciplined, verifiable reasoners.

This is the work of building a true foundation for intelligence, grounded in a symbolic source of truth. It is the next frontier toward the next generation of intelligent systems.

### References

\[1\] Original paper from [arXiv](https://arxiv.org/abs/2508.17906) and from [Hugging Face](https://huggingface.co/papers/2508.17906).

\[2\] Open source KG dataset from [Hugging Face](https://huggingface.co/datasets/domyn/FinReflectKG).