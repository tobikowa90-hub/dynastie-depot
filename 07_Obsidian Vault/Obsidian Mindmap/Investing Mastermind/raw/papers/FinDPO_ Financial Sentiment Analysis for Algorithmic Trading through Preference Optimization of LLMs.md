---
title: "FinDPO: Financial Sentiment Analysis for Algorithmic Trading through Preference Optimization of LLMs"
source: "https://arxiv.org/html/2507.18417v1"
author:
published:
created: 2026-04-20
description:
tags:
  - "clippings"
---
Giorgos Iacovides [giorgos.iacovides20@imperial.ac.uk](mailto:giorgos.iacovides20@imperial.ac.uk) Imperial College LondonLondonUK, Wuyang Zhou [wuyang.zhou19@imperial.ac.uk](mailto:wuyang.zhou19@imperial.ac.uk) Imperial College LondonLondonUK and Danilo Mandic [d.mandic@imperial.ac.uk](mailto:d.mandic@imperial.ac.uk) Imperial College LondonLondonUK

###### Abstract.

Opinions expressed in online finance-related textual data are having an increasingly profound impact on trading decisions and market movements. This trend highlights the vital role of sentiment analysis as a tool for quantifying the nature and strength of such opinions. With the rapid development of Generative AI (GenAI), supervised fine-tuned (SFT) large language models (LLMs) have become the de facto standard for financial sentiment analysis. However, the SFT paradigm can lead to memorization of the training data and often fails to generalize to unseen samples. This is a critical limitation in financial domains, where models must adapt to previously unobserved events and the nuanced, domain-specific language of finance. To this end, we introduce FinDPO, the first finance-specific LLM framework based on post-training human preference alignment via Direct Preference Optimization (DPO). The proposed FinDPO achieves state-of-the-art performance on standard sentiment classification benchmarks, outperforming existing supervised fine-tuned models by 11% on the average. Uniquely, the FinDPO framework enables the integration of a fine-tuned causal LLM into realistic portfolio strategies through a novel ‘logit-to-score’ conversion, which transforms discrete sentiment predictions into continuous, rankable sentiment scores (probabilities). In this way, simulations demonstrate that FinDPO is the first sentiment-based approach to maintain substantial positive returns of 67% annually and strong risk-adjusted performance, as indicated by a Sharpe ratio of 2.0, even under realistic transaction costs of 5 basis points (bps).

Large language models, sentiment analysis, direct preference optimization, algorithmic trading, portfolio construction.

## 1\. Introduction

Financial sentiment analysis refers to the quantification of opinions present in unlabeled textual data, and aims to categorize whether the overall perspective is positive, negative, or neutral - the so called valence. Given the rapidly increasing volume of financial sentiment-related textual information, and its readily available nature, it comes as no surprise that it has a significant influence on financial markets. This, coupled with the key role of algorithmic trading in quantitative finance, has highlighted the need for reliable and actionable AI models which are trained on such vast, multimodal data streams. Of particular interest to sentiment analysis is generative AI (GenAI), owing to its ability to recognize sentiment from textual sources such as news articles, earnings calls, financial reports, and other non-numerical data. The capacity of GenAI to operate on large-scale information sources makes it possible to capture macroscopic trends, promising a competitive edge in stock price prediction [^20] and the development of effective and robust trading strategies [^30].

Despite unquestionable conceptual benefits, the diverse, nuanced, and domain-specific nature of financial text poses significant challenges when it comes to accurate and actionable sentiment extraction. This underscores the need for context-aware sentiment analysis and highlights the non-trivial obstacles of employing natural language processing (NLP) in financial applications. Large language models (LLMs) have emerged as powerful tools for addressing these challenges, particularly when fine-tuned on labeled financial datasets through post-training techniques. Indeed, supervised fine-tuning (SFT) methods, particularly instruction tuning, which utilize the remarkable capability of LLMs to comprehend and generate human-like text, have become the de facto standard for enhancing the performance of pre-trained LLMs on financial sentiment classification tasks. Despite the initial success, recent work has shown that the SFT paradigm can lead to memorization of the training data while struggling to generalize to unseen samples [^4]. This limitation is particularly critical in financial domains, where the ability to generalize to previously unseen events is essential for robust algorithmic trading strategies. It also stands in stark contrast to the behavior of human financial analysts, who are able to extrapolate from limited prior information and apply domain knowledge to assess sentiment in new and unexpected market conditions.

![Refer to caption](https://arxiv.org/html/2507.18417v1/x1.png)

Figure 1. FinDPO training principle. Preference pairs are first generated from finance-specific labeled datasets. These preference pairs are then fed into the policy LLM whose weights are updated and the reference LLM whose weights are frozen. The weights of the policy LLM are updated by backpropagating the DPO loss, computed as the difference between the log-ratios of the policy and reference model probabilities for the preferred (correct) and dispreferred (incorrect) sentiment labels, as detailed in Equation 1. Intuitively, these updates encourage the policy model to increase the likelihood of selecting preferred sentiment labels while decreasing the likelihood of selecting dispreferred ones.

To address these issues, we set out to answer:

- Can we develop a financial sentiment analysis framework which goes beyond supervised fine-tuning and aligns large language models with human preferences as a means to enhance algorithmic trading?
- Can this be achieved in a way which does not require extensive computational resources, typically required by LLM post-training techniques, thus making the approach operational on standard computational resources?

To this end, we introduce the first post-training human preference alignment technique for financial sentiment analysis, based on Direct Preference Optimization (DPO) [^21]. This allows us to leverage human-alignment methods, which have demonstrated improved generalization to out-of-distribution inputs in other NLP tasks [^4], such as translation and summarization, in the financial domain. In particular, our solution, termed FinDPO, combines human preference optimization with a pre-trained LLM (specifically, Llama-3-8B Instruct [^7]) for financial sentiment analysis, enabling effective training on a small corpus of specialized, labeled, and publicly available financial news datasets. In this way, FinDPO achieves its ultimate goal of enhancing financial sentiment analysis through parameter-efficient DPO, while also minimizing computational resource requirements.

The main contributions of this work are therefore:

- We propose FinDPO, the first LLM aligned with human preferences specifically for financial sentiment analysis.
- The FinDPO approach does not require multiple high-end GPUs and can operate on standard computational resources. By leveraging the pre-trained Llama-3-8B model and employing parameter-efficient techniques within the DPO training, the computational demands typically associated with preference alignment approaches are dramatically reduced.
- The proposed framework enables, for the first time, causal LLMs to be integrated into long-short portfolio strategies by converting their discrete sentiment labels into continuous scores. This allows for evaluation through finance-specific, real-world performance metrics.
- Simulations demonstrate that FinDPO achieves substantial improvements in performance over existing state-of-the-art SFT models in both standard classification benchmarks and real-world financial metrics.

###### Remark 1.

Finance-specific causal LLMs have shown the most promising performance in sentiment classification tasks, however, they have not yet adequately addressed the domain of portfolio construction. By moving beyond traditional supervised fine-tuning toward human-aligned LLMs, and enabling the benchmarking of causal LLMs through algorithmic trading metrics, the contributions of our work promise to establish a paradigm shift in financial sentiment analysis.

## 2\. Related Work

Post-Training Techniques in Large Language Models. Even though LLMs trained on massive textual corpora possess remarkable general capabilities, their performance on downstream tasks can be significantly improved through post-training fine-tuning techniques. Post-training approaches typically fall into two categories: i) supervised fine-tuning (SFT), including instruction tuning, which adapts a pre-trained LLM using labeled input-output pairs, and ii) preference optimization. Despite success, instruction tuning remains limited in its ability to capture nuanced user preferences. Consequently, human preference optimization was introduced, initially through Reinforcement Learning from Human Feedback (RLHF) [^19]. This approach typically involves first training a reward model on a dataset of human preferences, and then fine-tuning the language model to maximize this reward using reinforcement learning algorithms, most commonly REINFORCE [^27], Proximal Policy Optimization (PPO) [^23], or their variants [^22]. While RLHF has demonstrated superior performance compared to instruction tuning, it is often computationally expensive and can be unstable due to the challenges of reward modeling and the complexity of the RL optimization process.

To mitigate these challenges, Direct Preference Optimization (DPO) [^21] has been proposed as a simpler, RL–free, and more stable alternative for training language models from preference data. Importantly, while DPO implicitly optimizes the same objective as RLHF (maximizing reward subject to a KL-divergence constraint), it achieves this in a direct and more tractable manner, maintaining ease of implementation and training stability.  
  
Sentiment Analysis with Large Language Models. The advent of transformer-based models for financial sentiment analysis began with FinBERT [^2], a variant of BERT fine-tuned on financial text, which demonstrated promising performance for sentiment classification tasks in the financial domain. However, FinBERT suffers from limitations such as insensitivity to numerical values, while due to its relatively small size (110 million parameters) its classification accuracy deteriorates with increased sentence complexity [^6]. More recently, Instruct-FinGPT [^29] and FinGPT [^25] models have adopted instruction tuning to enhance model performance, by leveraging the Llama-7B and Llama-2-13B models, respectively, as their base model. While these models represent a shift towards more powerful and generalizable LLMs, FinGPT is not specifically optimized for financial sentiment analysis. Furthermore, both models are limited to predicting sentiment valence (i.e., positive, negative, or neutral) but lack the ability to quantify the strength of a sentiment class, an essential parameter for portfolio construction.

In contrast, FinLlama [^11] combines SFT with the Llama-2-7B model and introduces a classification head at the output of the LLM to produce continuous sentiment scores. While this modification enables the sentiment signal to be integrated directly into portfolio construction workflows, it also shifts the primary objective of the model from next-token prediction to classification. This restricts the applicability of more advanced post-training techniques that depend on the generative capabilities of language models.

To address these limitations we propose FinDPO, the first finance-specific LLM for sentiment analysis based on post-training human preference alignment, rather than SFT. Our model is motivated by the fact that preference optimization has shown superior performance and generalization over SFT, particularly in tasks that involve capturing subtle human preferences expressed in nuanced language [^21] [^19], a characteristic that also underpins our task of financial sentiment classification.

## 3\. Preliminaries

Given dataset $\mathcal{D}$, the objective of DPO is to minimize

$$
\small\mathcal{L}_{\mathrm{DPO}}=-\mathbb{E}_{(\tilde{x},y^{w},y^{l})}\left[%
\log\sigma\left(\beta\cdot\left(\log\frac{\pi_{\theta}(y^{w}|\tilde{x})}{\pi_{%
\mathrm{ref}}(y^{w}|\tilde{x})}-\log\frac{\pi_{\theta}(y^{l}|\tilde{x})}{\pi_{%
\mathrm{ref}}(y^{l}|\tilde{x})}\right)\right)\right],
$$

where $\sigma$ denotes the nonlinear sigmoid function, and $\beta$ controls the deviation from the base reference policy, $\pi_{\mathrm{ref}}$, namely the initial reference LLM.

The typical workflow of DPO is outlined below:

1. For each prompt, $\tilde{x}$, sample completions $y_{1},y_{2}\sim\pi_{\mathrm{ref}}(\cdot|\tilde{x})$.
2. Collect human preference labels indicating which of $y_{1}$ or $y_{2}$ is preferred, yielding an offline dataset of preference pairs $\mathcal{D}=\{(\tilde{x}_{i},y_{i}^{w},y_{i}^{l})\}_{i=1}^{N}$.
3. Optimize the policy (trainable) model, $\pi_{\theta}$, to minimize the DPO loss given the reference (frozen) model, $\pi_{\mathrm{ref}}$, the dataset, $\mathcal{D}$, and the desired hyperparameter, $\beta$.

Intuitively, DPO updates the parameters of the policy model, $\pi_{\theta}$, to increase the likelihood of preferred responses, $y^{w}$, and decrease the likelihood of dispreferred responses, $y^{l}$. The magnitude of these updates is modulated by how strongly $\pi_{\theta}$ disagrees with human preferences, scaled by $\beta$. This dynamic weighting stabilizes training and prevents model collapse.

## 4\. Methodology

Our work aims to leverage the expressive power and contextual understanding of general-purpose LLMs and adapt them for sentiment analysis applications. This is achieved by applying human preference alignment, using DPO, to Llama-3-8B-Instruct, which designates our $\pi_{\mathrm{ref}}$ model, and aligning it on a finance-specific corpus. The effectiveness of our approach is evaluated in two ways. First, we assess the performance of the model relative to other finance-specific LLMs using standard classification-focused benchmarks, such as the weighted F1 score. For rigour, our model is further evaluated through a set of benchmarks that closely align with real-world portfolio construction — the ultimate goal of sentiment analysis.

### 4.1. Training Pipeline of FinDPO

Pre-trained LLMs offer a range of capabilities such as reasoning, translation, summarization, and text generation, however, they often struggle when applied directly to domain-specific tasks such as financial sentiment analysis. This limitation is particularly pronounced in the finance domain, where nuanced language, speculative narratives, and the extensive length of financial news articles pose significant challenges for general-purpose models.

To address these challenges, our work revisits the first principles of LLMs and leverages human preference alignment to adapt them for financial sentiment analysis. More specifically, we utilize DPO, which operates directly on pairwise preferences constructed from ground-truth sentiment labels and model predictions, enabling the model to learn fine-grained distinctions in financial sentiment while preserving its generative capabilities. Through this process, the proposed FinDPO model produces sentiment predictions for three classes: positive, negative, or neutral.

#### 4.1.1. Training Datasets.

The training data consisted of three publicly available labeled financial news datasets, obtained from HuggingFace: the Financial PhraseBank (FPB) dataset [^18], the Twitter Financial News dataset [^26], and the GPT-labeled Financial News dataset [^17]. This resulted in a total of 32,970 labeled samples, of which 80% were used for training and the remaining 20% for testing. The datasets are summarized below.

- Financial PhraseBank (FPB) Dataset. The FPB dataset consists of 4,840 samples which were randomly extracted from financial news articles. In order to ensure high quality annotation, the samples were annotated by 16 experts with backgrounds in finance and business. Each sample was annotated with one of the three labels: positive, negative, and neutral.
- Twitter Financial News Sentiment (TFNS). The TFNS dataset includes 11,930 tweets with content from the financial domain. Each tweet was annotated as positive, negative, and neutral.
- GPT-labelled Financial News (NWGI). The NWGI dataset consists of 16,200 financial news articles. Each article was annotated with one of the five labels: strongly negative, mildly negative, neutral, mildly positive, and strongly positive. To align this dataset with the three-class structure of the other datasets, the strongly and mildly negative classes were combined into a single negative class, and similarly, the strongly and mildly positive classes were combined into a single positive class.

As DPO requires preference pairs rather than class labels, we converted those three datasets into synthetic pairwise preference data. Each raw text input, $x_{i}$, was first converted into its instruction format, $\tilde{x}_{i}$, compatible with the instruction-tuned model. For each sample, we set the preferred response, $y^{w}_{i}$, to the ground-truth sentiment label. To obtain the dispreferred response, $y^{l}_{i}$, we prompted the reference model, $\pi_{\mathrm{ref}}$, with $\tilde{x}_{i}$ to generate sentiment predictions. If the prediction matched the ground-truth sentiment label, we randomly sampled a different incorrect label as $y^{l}_{i}$ to avoid bias in selecting the dispreferred response. If the prediction was incorrect, we used the predicted label as $y^{l}_{i}$ in order to guide the model away from its own mistakes and reinforce correct sentiment predictions. This resulted in a dataset of preference pairs $\mathcal{D}=\{(\tilde{x}_{i},y^{w}_{i},y^{l}_{i})\}_{i=1}^{N}$, which was used for DPO training.

#### 4.1.2. Model Training.

The proposed FinDPO model was first initialized with the Llama-3-8B-Instruct model, which serves as the base reference policy, $\pi_{\mathrm{ref}}$, followed by DPO alignment over 5 epochs. The training process employed the AdamW optimizer [^15], as it effectively decouples the weight decay from the optimization steps and leads to more stable convergence. The initial learning rate was deliberately set to a small value as the Llama-3 model is already pre-trained on a large corpus of data, whilst the warm-up ratio and weight decay served as key regularization techniques to prevent overfitting, a crucial aspect given the limited size of our DPO training dataset.

Furthermore, Low-Rank Adaptation (LoRA) [^9] was integrated into the DPO training with a rank $r=16$, scaling factor $\alpha=16$, and dropout rate of 0.05, in order to minimize the number of trainable parameters while maintaining high end performance. Through the LoRA implementation, the number of trainable parameters was set to 41.9M, amounting to just 0.52% of the total number of parameters in the base model. This made it possible for our training process to be implemented on a single A100 (40 GB) GPU, thus avoiding the need for excessive computational resources. The full training procedure was completed in 4.5 hours on an A100 (40 GB) GPU.

The entire training pipeline, including the conversion of raw training data into a dataset of preference pairs, $\mathcal{D}$, and the subsequent DPO alignment of the base reference policy, $\pi_{\mathrm{ref}}$, on $\mathcal{D}$ to produce our FinDPO model, is given in Figure 1.

### 4.2. Proposed Framework for Sentiment-Driven Portfolio Construction

Once our FinDPO model was established, we followed the framework illustrated in Figure 2. The objective of our framework was to evaluate the performance of FinDPO against other established sentiment analysis methods using finance-specific real-world metrics, offering a more practical assessment of model utility for portfolio construction.

![Refer to caption](https://arxiv.org/html/2507.18417v1/x2.png)

Figure 2. Proposed framework for our sentiment-driven portfolio construction. The ‘logit-to-score’ converter is only required for the finance-specific causal LLMs.

Data Collection. Both textual and market data were collected to support the construction of appropriate long-short (L/S) portfolios. For the textual data, 204,017 financial news articles dating between February 2015 and June 2021 were gathered from reputable online sources, including Reuters, The Motley Fool, and MarketWatch. These sources were chosen for their reliability, reputation, low bias, and focus on major corporations. For the same period, the corresponding financial market data were obtained from Yahoo Finance, comprising daily stock returns for the 500 companies in our Investable Universe (S&P 500). This resulted in 1,672 days of stock return data per company.

Named Entity Recognition. To ensure that news articles are accurately linked to the correct organizational entity, each article must be associated with at least one relevant stock [^5]. This step reduces the likelihood of irrelevant articles being connected to a particular stock [^3]. For robustness, in our study we employed the BERT-base-NER model [^14], which is capable of recognizing four types of entities: location, organization, person, and miscellaneous, and provides a confidence score for each identified entity. For each article in our corpus, if the confidence score for the entity associated with the company exceeded 98%, the article was retained; otherwise, it was discarded. Table 1 presents the results of applying the NER filtering on the initially scraped dataset in terms of the number of articles retained. Observe that this process reduced the total number of articles by 24.1%. The effect was similar for MarketWatch and The Motley Fool, with both exhibiting reductions of around 25%, while Reuters experienced a smaller decrease of approximately 6.3%.

Table 1. Total number of articles obtained per source before and after NER filtering, with percentage reduction shown in brackets.

| News Source | No. of articles pre processing | No. of articles post NER filtering |
| --- | --- | --- |
| MarketWatch | 309,187 | 236,214 (23.6%) |
| Reuters | 38,141 | 35,741 (6.3%) |
| The Motley Fool | 205,270 | 147,413 (28.2%) |
| Total | 552,598 | 419,368 (24.1%) |

Text Pre-Processing: Each news article was represented using a bag-of-words approach, and the following steps were subsequently performed: a) Tokenization, b) Stop-Word Removal, c) Lemmatization, d) (Lower) Case Normalization, and e) Feature Selection. For the Feature Selection step, the frequency of each word was used as the primary feature, particularly in the lexicon-based approaches.

Sentiment Analysis. In total, five sentiment analysis methods were used as baselines for comparison with our FinDPO model. These consisted of lexicon-based approaches and SFT classification LLMs, including the existing SOTA FinLlama [^11]. Among the lexicon-based methods, LMD [^16] and HIV-4 [^24] were implemented using the pysentiment2 Python library, while VADER [^10] was implemented using the NLTK library. For SFT classification models, we evaluated FinBERT [^2] and FinLlama [^11], obtained through HuggingFace and utilized via the Transformers library.

Despite exhibiting the strongest performance on standard classification focused benchmarks (as shown in Table 2), fine-tuned causal LLMs are inherently limited to generating discrete sentiment labels (i.e., positive, negative, neutral) and do not capture the sentiment strength. However, understanding how strongly a sentiment is expressed is crucial for portfolio construction, where assets must be ranked based on sentiment magnitude rather than simply classified into categories. To overcome this limitation and demonstrate the feasibility of using causal LLMs for portfolio construction, we propose a novel ‘logit-to-score’ converter within our FinDPO framework, which enables sentiment strength ranking by leveraging the internal representations of the model.

###### Remark 2.

To make causal LLMs amenable to portfolio construction, we extract the logits of the model corresponding to the first generated token, which represents the predicted sentiment class, and apply a softmax function over the logits associated with the predefined sentiment classes (i.e., ‘positive’, ‘negative’, or ‘neutral’). This results in a normalized probability distribution over the sentiment labels, which we interpret as sentiment scores suitable for ranking assets in a portfolio.

Related to our FinDPO model, prior work has shown that preference aligned LLMs can exhibit overconfidence [^13]. We have also observed this effect in our model, whereby it consistently assigned a probability of 1.0 to the predicted valence class and 0.0 to the other two valence classes. To mitigate this and produce more meaningful probabilistic sentiment scores, we employed temperature scaling [^8], a post-hoc calibration method. The temperature parameter $T$ was optimized on the training set by minimizing the negative log-likelihood (NLL). This calibration was performed independently of the financial article corpus used for portfolio construction, ensuring no data leakage.

The considered methods were evaluated on every article within each corpus for a given company. In cases where multiple articles were published on the same day for a given company, the average sentiment for that day was calculated as

$$
S_{t}=\frac{1}{N_{t}}\sum_{i=1}^{N_{t}}S_{it}
$$

Here, $S_{t}$ represents the average sentiment for the t-th day, $N_{t}$ denotes the number of news articles published on that same t-th day for a given company, while $S_{it}$ designates the sentiment strength of the i-th news article on a particular t-th day. The daily sentiment outputs for each company were merged to arrive at the final sentiment data that were utilized as a parameter in the portfolio construction stage.

Portfolio Construction. Once the sentiment for each method was defined for every company, the long-short portfolio was constructed. We used the sentiment as a parameter to determine which companies should be in a long or a short position, aiming to maximize returns from both positions. The long-short portfolio was constructed using the following procedure:

- Define the Investable Universe: Even though the S&P 500 comprises 500 companies, the financial textual data collected did not contain articles associated to some of the companies for the test period of February 2015 to June 2021. Consequently, 417 companies were considered.
- Define the long and short position: The sentiment signal obtained from each of the six methods was used to construct six distinct portfolios. For each method, companies were ranked daily according to their sentiment. Companies that did not have sentiment data on a particular day were omitted from the ranking. As the daily sentiment score for each company ranges between -1 and 1, those with the highest positive sentiment were placed in a long position, while those with the strongest negative sentiment were placed in a short position.
- Allocation: An equally-weighted portfolio strategy was considered in our portfolio construction as this strategy is mostly utilized by hedge funds [^12]. Similar to [^11], the percentage of companies in a long and short position was fixed at 35%. Consequently, the top 35% of companies in terms of performance were allocated to long positions, while the bottom 35% were allocated to short positions.
- Determine daily returns: The daily return for each company that was held in a long or short position was obtained by the market data on that particular day. The average daily return of companies that were held in a long position, $r_{Long}$, was defined as
	$$
	r_{Long}=\frac{1}{N_{Long}}\sum_{i=1}^{N_{Long}}r_{Long}(i)
	$$
	Similarly, the average daily return of companies that were held in a short position, $r_{Short}$, was defined as
	$$
	r_{Short}=\frac{1}{N_{Short}}\sum_{i=1}^{N_{Short}}r_{Short}(i)
	$$
	For each particular day, the number of companies that were held in either a long position ($N_{Long}$) or a short position ($N_{Short}$) were equal. Consequently, the total portfolio return on a particular day is the difference between the daily long return, $r_{Long}(i)$, and daily short return, $r_{Short}(i)$, and is given by
	$$
	r_{daily}(i)=r_{Long}(i)-r_{Short}(i)
	$$

Portfolio Evaluation. The performance of the portfolio constructed using the proposed model was assessed against the portfolios constructed using the other sentiment methods. We considered:

- Profitability, via cumulative returns, $r_{\text{cum}}$, and annualized returns, $R_{p}$, defined as
	$$
	r_{\text{cum}}=\sum_{i=1}^{N}r_{\text{daily}}(i)
	$$
	 
	$$
	R_{p}=\frac{1}{N}\sum_{i=1}^{N}r_{\text{log}}(i)\cdot 252
	$$
- Risk-adjusted performance, through annualized Sharpe, $S_{a}$, Sortino, $S_{o}$, and Calmar, $C_{r}$, ratios, defined as
	$$
	S_{a}=\frac{R_{p}-R_{f}}{\sigma_{p}}
	$$
	 
	$$
	S_{o}=\frac{\bar{r}_{\text{simple}}-R_{f}}{\sigma_{d}}\cdot\sqrt{252}
	$$
	 
	$$
	C_{r}=\frac{(1+\bar{r}_{\text{simple}})^{252}-1}{\text{MDD}}
	$$

Here, $N$ is the total number of trading days, totaling 1,672, $r_{\text{log}}(i)$ represents the daily logarithmic return, and $\bar{r}_{\text{simple}}$ denotes the average daily simple return. The symbol $R_{f}$ is the annualized risk-free rate of return, $\sigma_{p}$ is the annualized volatility, $\sigma_{d}$ is the downside deviation of daily returns, and MDD is the maximum drawdown. The constant 252 corresponds to the number of business days in a calendar year. The risk-free return, $R_{f}$, typically represents the yield of the 10-Year Treasury Note; however, due to its prolonged low yield during the analyzed period [^28], a 0% rate is commonly used and was adopted in our analysis.

## 5\. Experimental Results

We evaluated the effectiveness of our proposed FinDPO framework through both machine learning and financial performance assessments. The machine-learning evaluation focused on standard sentiment classification benchmarks to measure predictive performance. The financial evaluation examined the real-world utility of FinDPO by integrating its outputs into an algorithmic trading strategy and analyzing portfolio performance under both idealized and realistic market conditions.

### 5.1. Evaluation via Classification Metrics

The performance of our FinDPO model was assessed by first evaluating it on the test splits of the three datasets used for training, which are considered the standard benchmarks in financial sentiment analysis, using the weighted F1 score. Our model was compared against classical lexicon-based methods, as well as FinBERT and Instruct-FinGPT. In addition, we compared FinDPO against the state-of-the-art models in financial sentiment analysis, namely FinLlama and FinGPT v3.3. To further evaluate the effectiveness of DPO relative to instruction tuning – the most prominent approach for improving financial sentiment classification in general-purpose LLMs (as demonstrated in FinGPT v3.3) – we compared FinDPO to its instruction-tuned counterpart, using the same base model, which we refer to as FinSFT.

Table 2. Weighted F1 scores of the evaluated sentiment-based methods on the FPB, TFNS, and NWGI financial sentiment datasets. HIV-4, VADER, and LMD are lexicon-based baselines. FinBERT and FinLlama are SFT classification LLMs, while Instruct-FinGPT, FinGPT v3.3 and FinSFT are instruction-tuned causal LLMs. FinDPO is our proposed DPO-aligned causal LLM. FinBERT is excluded from evaluation on FPB due to data leakage, as it was originally trained on the full FPB dataset.

| Model | FPB | TFNS | NWGI | Average |
| --- | --- | --- | --- | --- |
| HIV-4 | 0.357 | 0.401 | 0.384 | 0.385 |
| VADER | 0.536 | 0.518 | 0.462 | 0.491 |
| LMD | 0.546 | 0.572 | 0.440 | 0.498 |
| FinBERT | — | 0.733 | 0.538 | 0.611 |
| FinLlama | 0.707 | 0.904 | 0.538 | 0.679 |
| Instruct-FinGPT | 0.777 | 0.828 | 0.583 | 0.690 |
| FinGPT v3.3 | 0.879 | 0.903 | 0.643 | 0.762 |
| FinSFT | 0.829 | 0.850 | 0.708 | 0.771 |
| FinDPO (Ours) | 0.865 | 0.872 | 0.833 | 0.846 |

Table 2 shows that FinDPO achieves the highest average performance across all three benchmark datasets, with a weighted F1 score of 0.846, outperforming FinGPT v3.3, the state-of-the-art model in financial sentiment classification, by 11%. Notably, FinSFT delivers performance comparable to FinGPT v3.3, despite being based on the newer Llama-3-8B model rather than Llama-2-13B, suggesting that instruction-tuned models have reached a performance ceiling. This comparison highlights that the superior performance of FinDPO is not due to a more powerful base model, but rather to the use of our sentiment-specific DPO framework, which aligns model outputs with ground truth labels more effectively than instruction tuning in the context of financial sentiment classification.

###### Remark 3.

The introduced DPO not only encourages the LLM to increase the likelihood of preferred sentiment labels but also explicitly penalizes the selection of dispreferred ones, resulting in better generalization to unseen samples compared to SFT methods which solely optimize for correct predictions.

![Refer to caption](https://arxiv.org/html/2507.18417v1/x3.png)

Figure 3. Cumulative returns of sentiment-based long-short portfolios at 0 and 5 bps transaction costs, compared against the S&P 500 benchmark.

### 5.2. Evaluation via Real-World Financial Metrics

We next assessed the performances of the six portfolios which were constructed as described in Section 4.2, without accounting for transaction costs. These are illustrated in the left panel of Figure 3 and Table 3. Observe that our proposed method, FinDPO, significantly outperforms the existing state-of-the-art model in sentiment-based portfolio construction, FinLlama, achieving a 187% improvement in cumulative returns. Critically, FinDPO also demonstrates superior risk-adjusted performance, with an increase of 1.1 in the Sharpe ratio, indicating a more favorable return-to-volatility trade-off. Furthermore, FinDPO achieves the highest Sortino and Calmar ratios (6.05 and 11.94, respectively), reflecting improved downside risk control and a stronger reward-to-drawdown profile, both of which are key considerations for risk-averse investors.

It is important to note that, in this idealized evaluation setting where transaction costs are not considered, all methods, including lexicon-based approaches, exhibit relatively strong performance. This highlights a key limitation of much of the existing literature, where sentiment-driven portfolio strategies are evaluated under frictionless assumptions. Such settings can lead to overly optimistic conclusions that may not hold in real-world trading environments, where transaction costs can significantly affect performance.

Table 3. Performance metrics of the sentiment-based portfolios at no transaction cost. For each metric, the best performance is shown in bold, and the second-best is underlined.

| Method | Cumulative Return (%) | Annualized Return (%) | Sharpe | Sortino | Calmar |
| --- | --- | --- | --- | --- | --- |
| S&P 500 | 83.12 | 11.34 | 0.62 | 0.81 | 0.41 |
| HIV-4 | 90.07 | 12.88 | 0.81 | 1.25 | 0.67 |
| VADER | 82.81 | 11.76 | 0.75 | 1.21 | 0.34 |
| LMD | 139.88 | 20.62 | 1.26 | 1.96 | 1.17 |
| FinBERT | 199.19 | 29.64 | 1.65 | 2.39 | 1.24 |
| FinLlama | 260.74 | 39.47 | 2.33 | 3.48 | 3.30 |
| FinDPO (Ours) | 747.10 | 111.78 | 3.41 | 6.05 | 11.94 |

### 5.3. Incorporating Transaction Costs into Portfolio Construction

We further assessed the impact of transaction costs on portfolio performance to better reflect practical trading conditions. In real-world settings, these costs can significantly reduce returns, especially for high-turnover strategies such as the daily rebalancing strategy we followed. Given that our investable universe consisted of relatively liquid instruments, specifically the S&P 500 constituents, we varied the transaction cost parameter $k$ from 1 to 5 basis points (bps), which aligns with the typical 2–5 bps range observed in U.S. equities. To incorporate transaction costs, we adjusted daily portfolio returns using the standard linear model as

$$
r_{t}=R_{t}-k\cdot\text{Turnover}_{t},
$$

where $R_{t}$ is the unadjusted portfolio return on day $t$, and

$$
\text{Turnover}_{t}=\sum_{i}\left|w_{t}^{(i)}-w_{t-1}^{(i)}\right|
$$

represents the total absolute change in portfolio weights across all assets, accounting for both long and short positions.

Table 4. Profitability and risk-adjusted performance of the portfolios constructed by the six sentiment-based methods across different transaction cost levels. For all metrics, higher values indicate better performance. Positive (desired) values are highlighted in green and negative (undesired) values are highlighted in red. For each metric and cost level, the best performance is shown in bold, and the second-best is underlined.

<table><tbody><tr><td>Cost (bps)</td><td>Method</td><td>Cumulative Return (%)</td><td>Annualized Return (%)</td><td>Sharpe</td><td>Sortino</td><td>Calmar</td></tr><tr><td></td><td>S&P 500</td><td>83.12</td><td>11.34</td><td>0.62</td><td>0.81</td><td>0.41</td></tr><tr><td rowspan="6">1.0</td><td>HIV-4</td><td>36.17</td><td>4.41</td><td>0.28</td><td>0.50</td><td>0.21</td></tr><tr><td>VADER</td><td>29.32</td><td>3.37</td><td>0.21</td><td>0.43</td><td>0.09</td></tr><tr><td>LMD</td><td>85.54</td><td>12.09</td><td>0.74</td><td>1.20</td><td>0.52</td></tr><tr><td>FinBERT</td><td>144.46</td><td>21.06</td><td>1.17</td><td>1.74</td><td>0.71</td></tr><tr><td>FinLlama</td><td>205.16</td><td>30.75</td><td>1.81</td><td>2.75</td><td>2.05</td></tr><tr><td>FinDPO (Ours)</td><td>689.48</td><td>102.76</td><td>3.14</td><td>5.61</td><td>8.04</td></tr><tr><td rowspan="6">2.0</td><td>HIV-4</td><td>-17.74</td><td>-4.05</td><td>-0.26</td><td>-0.25</td><td>-0.07</td></tr><tr><td>VADER</td><td>-24.16</td><td>-5.03</td><td>-0.32</td><td>-0.35</td><td>-0.06</td></tr><tr><td>LMD</td><td>31.20</td><td>3.56</td><td>0.22</td><td>0.44</td><td>0.15</td></tr><tr><td>FinBERT</td><td>89.72</td><td>12.47</td><td>0.69</td><td>1.08</td><td>0.37</td></tr><tr><td>FinLlama</td><td>149.59</td><td>22.04</td><td>1.30</td><td>2.00</td><td>1.03</td></tr><tr><td>FinDPO (Ours)</td><td>631.85</td><td>93.73</td><td>2.86</td><td>5.15</td><td>5.47</td></tr><tr><td rowspan="6">3.0</td><td>HIV-4</td><td>-71.64</td><td>-12.52</td><td>-0.79</td><td>-0.99</td><td>-0.17</td></tr><tr><td>VADER</td><td>-77.64</td><td>-13.43</td><td>-0.85</td><td>-1.13</td><td>-0.16</td></tr><tr><td>LMD</td><td>-23.14</td><td>-4.97</td><td>-0.30</td><td>-0.32</td><td>-0.09</td></tr><tr><td>FinBERT</td><td>34.99</td><td>3.88</td><td>0.22</td><td>0.42</td><td>0.12</td></tr><tr><td>FinLlama</td><td>94.02</td><td>13.32</td><td>0.79</td><td>1.26</td><td>0.49</td></tr><tr><td>FinDPO (Ours)</td><td>574.22</td><td>84.71</td><td>2.59</td><td>4.69</td><td>3.94</td></tr><tr><td rowspan="6">4.0</td><td>HIV-4</td><td>-125.55</td><td>-20.99</td><td>-1.32</td><td>-1.73</td><td>-0.23</td></tr><tr><td>VADER</td><td>-131.13</td><td>-21.84</td><td>-1.39</td><td>-1.90</td><td>-0.23</td></tr><tr><td>LMD</td><td>-77.49</td><td>-13.51</td><td>-0.83</td><td>-1.08</td><td>-0.19</td></tr><tr><td>FinBERT</td><td>-19.74</td><td>-4.72</td><td>-0.26</td><td>-0.24</td><td>-0.06</td></tr><tr><td>FinLlama</td><td>38.44</td><td>4.60</td><td>0.27</td><td>0.52</td><td>0.16</td></tr><tr><td>FinDPO</td><td>516.59</td><td>75.68</td><td>2.31</td><td>4.22</td><td>2.92</td></tr><tr><td rowspan="6">5.0</td><td>HIV-4</td><td>-179.46</td><td>-29.46</td><td>-1.85</td><td>-2.46</td><td>-0.28</td></tr><tr><td>VADER</td><td>-184.61</td><td>-30.24</td><td>-1.92</td><td>-2.66</td><td>-0.29</td></tr><tr><td>LMD</td><td>-131.83</td><td>-22.05</td><td>-1.35</td><td>-1.84</td><td>-0.25</td></tr><tr><td>FinBERT</td><td>-74.48</td><td>-13.31</td><td>-0.74</td><td>-0.90</td><td>-0.18</td></tr><tr><td>FinLlama</td><td>-17.13</td><td>-4.13</td><td>-0.24</td><td>-0.23</td><td>-0.06</td></tr><tr><td>FinDPO (Ours)</td><td>458.97</td><td>66.64</td><td>2.03</td><td>3.75</td><td>2.21</td></tr></tbody></table>

When transaction costs are considered, a clear performance gap emerges between FinDPO and all other sentiment-based portfolio construction methods. Even at a high transaction cost of 5 bps, FinDPO remained the only method that consistently delivered significant positive returns and robust risk-adjusted performance, achieving an annualized return of 67% with a Sharpe ratio of 2.0. In contrast, all other methods, including FinLlama, exhibited substantial degradation in both absolute and risk-adjusted performance, with all yielding very low to highly negative cumulative returns at realistic transaction cost levels of 4–5 bps. The inability of these methods to maintain profitability under transaction costs highlights their sensitivity to turnover and the lack of robustness in real-world trading environments.

In contrast, FinDPO demonstrates strong and stable performance across all transaction cost levels, underscoring its effectiveness at extracting robust trading signals and its resilience to market frictions. These results highlight that FinDPO is not only highly profitable under idealized conditions but also realistically deployable, maintaining high annualized returns and strong risk-adjusted performance even under challenging market conditions.

## 6\. Conclusion

We have introduced an innovative approach to financial sentiment analysis which rests upon Direct Preference Optimization (DPO), a post-training alignment technique based on human preference optimization. By leveraging the expressive power and contextual understanding of a pre-trained LLM and adapting it to financial sentiment analysis, this approach has enabled the model to become more attuned to the nuanced language of the financial domain, while also minimizing resource utilization and computational overhead. Owing to the strong generalization capability of preference-based alignment techniques compared to SFT approaches, including instruction tuning, our proposed FinDPO model has achieved a weighted F1 score that outperforms the SOTA FinGPT v3.3 model by 11% on the average.

Uniquely, our framework has enabled fine-tuned causal LLMs, which have shown superior performance on machine learning benchmarks, to be integrated into portfolio optimization strategies. This has allowed for the evaluation of our FinDPO model using real-world financial metrics, which extend beyond the traditional classification-focused evaluations currently found in the literature. Overall, these advantages have established FinDPO, to the best of our knowledge, as the first sentiment-based method to maintain substantial positive returns and strong risk-adjusted performance even under high transaction costs, thus making it robust and practically deployable in real-world trading environments.

Disclaimer: Nothing herein is financial advice, and NOT a recommendation to trade real money. Please use common sense and always first consult a professional before trading or investing.

###### Acknowledgements.

The authors would like to thank Thanos Konstantinidis, Portfolio Manager at Engineers Gate, for their valuable feedback and suggestions regarding portfolio construction and the calculation of transaction costs.

[^2]: Dogu Araci. 2019. FinBERT: Financial sentiment analysis with pre-trained language models. *arXiv preprint arXiv:1908.10063* (2019).

[^3]: Jacob Boudoukh, Ronen Feldman, Shimon Kogan, and Matthew Richardson. 2013. *Which news moves stock prices? A textual analysis*. Technical Report. National Bureau of Economic Research.

[^4]: Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie, Sergey Levine, and Yi Ma. 2025. SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training. In *The Second Conference on Parsimony and Learning (Recent Spotlight Track)*.

[^5]: Ronen Feldman, Benjamin Rosenfeld, Roy Bar-Haim, and Moshe Fresko. 2011. The stock sonar—sentiment analysis of stocks based on a hybrid approach. In *Proceedings of the AAAI Conference on Artificial Intelligence*, Vol. 25. 1642–1647.

[^6]: Sandro Gössi, Ziwei Chen, Wonseong Kim, Bernhard Bermeitinger, and Siegfried Handschuh. 2023. Finbert-fomc: Fine-tuned finbert model with sentiment focus method for enhancing sentiment analysis of fomc minutes. In *Proceedings of the Fourth ACM International Conference on AI in Finance*. 357–364.

[^7]: Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. 2024. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783* (2024).

[^8]: Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. 2017. On Calibration of Modern Neural Networks. In *Proceedings of the 34th International Conference on Machine Learning* *(Proceedings of Machine Learning Research, Vol. 70)*. PMLR, 1321–1330.

[^9]: Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2022. LoRA: Low-Rank Adaptation of Large Language Models. In *The Tenth International Conference on Learning Representations*.

[^10]: Clayton Hutto and Eric Gilbert. 2014. Vader: A parsimonious rule-based model for sentiment analysis of social media text. In *Proceedings of the international AAAI conference on web and social media*, Vol. 8. 216–225.

[^11]: Giorgos Iacovides, Thanos Konstantinidis, Mingxue Xu, and Danilo Mandic. 2024. FinLlama: LLM-Based Financial Sentiment Analysis for Algorithmic Trading. In *Proceedings of the 5th ACM International Conference on AI in Finance*. 134–141.

[^12]: Zheng Tracy Ke, Bryan T. Kelly, and Dacheng Xiu. 2019. *Predicting Returns With Text Data*. NBER Working Papers 26186. National Bureau of Economic Research, Inc. [https://EconPapers.repec.org/RePEc:nbr:nberwo:26186](https://econpapers.repec.org/RePEc:nbr:nberwo:26186)

[^13]: Jixuan Leng, Chengsong Huang, Banghua Zhu, and Jiaxin Huang. 2025. Taming Overconfidence in LLMs: Reward Calibration in RLHF. In *The Thirteenth International Conference on Learning Representations*.

[^14]: D. S. Lim. 2021. BERT-base-NER. [https://huggingface.co/dslim/bert-base-NER](https://huggingface.co/dslim/bert-base-NER).

[^15]: Ilya Loshchilov, Frank Hutter, et al. 2017. Fixing weight decay regularization in adam. *arXiv preprint arXiv:1711.05101* 5 (2017), 5.

[^16]: Tim Loughran and Bill Mcdonald. 2011. When Is a Liability NOT a Liability? Textual Analysis, Dictionaries, and 10-Ks. *The Journal of Finance* 66 (02 2011), 35 – 65.

[^17]: Neural Magic. 2022. Twitter Financial News Sentiment. [http://precog.iiitd.edu.in/people/anupama](http://precog.iiitd.edu.in/people/anupama)

[^18]: Pekka Malo, Ankur Sinha, Pekka Korhonen, Jyrki Wallenius, and Pyry Takala. 2014. Good debt or bad debt: Detecting semantic orientations in economic texts. *Journal of the Association for Information Science and Technology* 65, 4 (2014), 782–796.

[^19]: Long Ouyang et al. 2022. Training language models to follow instructions with human feedback. In *Proceedings of the 36th International Conference on Neural Information Processing Systems* (New Orleans, LA, USA) *(NIPS ’22)*. Article 2011, 15 pages.

[^20]: Yangtuo Peng and Hui Jiang. 2016. Leverage Financial News to Predict Stock Price Movements Using Word Embeddings and Deep Neural Networks. In *Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*. Association for Computational Linguistics, 374–379.

[^21]: Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. 2023. Direct Preference Optimization: Your Language Model is Secretly a Reward Model. In *Thirty-seventh Conference on Neural Information Processing Systems*.

[^22]: Rajkumar Ramamurthy et al. 2023. Is Reinforcement Learning (Not) for Natural Language Processing: Benchmarks, Baselines, and Building Blocks for Natural Language Policy Optimization. In *The Eleventh International Conference on Learning Representations*.

[^23]: John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 2017. Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347* (2017).

[^24]: P. J. Stone, D. C. Dunphy, M. S. Smith, and D. M. Ogilvie. 1966. *The General Inquirer: A Computer Approach to Content Analysis*. MIT Press.

[^25]: Neng Wang, Hongyang Yang, and Christina Dan Wang. 2023. FinGPT: Instruction Tuning Benchmark for Open-Source Large Language Models in Financial Datasets. *NeurIPS Workshop on Instruction Tuning and Instruction Following* (2023).

[^26]: Oliver Wang. 2023. News with GPT instructions. [https://huggingface.co/datasets/oliverwang15/news\_with\_gpt\_instructions](https://huggingface.co/datasets/oliverwang15/news_with_gpt_instructions)

[^27]: Ronald J. Williams. 2004. Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning. *Machine Learning* 8 (2004), 229–256.

[^28]: Yahoo Finance. 2023. Treasury yield 10 years historical data. [https://finance.yahoo.com/quote/%5ETNX/history](https://finance.yahoo.com/quote/%5ETNX/history)

[^29]: Boyu Zhang, Hongyang Yang, and Xiao-Yang Liu. 2023. Instruct-FinGPT: Financial Sentiment Analysis by Instruction Tuning of General-Purpose Large Language Models. *ArXiv* abs/2306.12659 (2023). [https://api.semanticscholar.org/CorpusID:259224880](https://api.semanticscholar.org/CorpusID:259224880)

[^30]: Wenbin Zhang and Steven Skiena. 2010. Trading Strategies to Exploit Blog and News Sentiment. *Proceedings of the International AAAI Conference on Web and Social Media* 4, 1 (May 2010), 375–378.