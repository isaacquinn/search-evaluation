# Search Engine Evaluation Report

## 1. Overview

This following report details the rationale and evaluation process of comparing two different versions of the search functionality on our AGENT platform. The goal of this evaluation is to assess which search system offers better <u>relevance</u> and <u>ranking quality</u>; we assessed this using industry-standard metrics drawn from information retrieval (IR) research (see **9. References**).

This evaluation is focused on two search functionalities:
1. **Dynamic relational search:** a key-based search currently employed on our platforms, referred to as **"OLD"**
2. **Vector database search:** a vector-based semantic search in testing, referred to as **"NEW"**

Limitation: The current search function *only* allows users to search from studies published on the platform. Eventually, it will return results across a combined catalog of studies, models, tools, and cohorts. For purposes of this evaluation, both search functions being compared will only be returning search results for studies published on the platform.


---

## 2. Evaluation Approach

Given time and resource constraints, a **human relevance judgment** approach was adopted, using # evaluators with knowledge of the domain. A set of representative queries was developed based on common user tasks and search goals. Each system's top 5 (or other #?) results for these queries were captured and scored manually for relevance.

### Metrics Used

We selected three well-established metrics from the information retrieval literature:

- **Precision@5 (P@5):**  
  Measures the proportion of relevant results in the top 5 results. Useful for judging immediate usefulness. [1, 2]

- **Mean Reciprocal Rank (MRR):**  
  Considers the rank position of the first relevant result. High MRR means users likely find a relevant item quickly. [3, 4]

- **Normalized Discounted Cumulative Gain at 5 (nDCG@5):**  
  Measures the usefulness of results ranked by position and graded relevance, with discounted value for lower-ranked relevant items. [5, 6, 7]

These metrics collectively capture both **accuracy** and **ranking quality**.

---

## 3. Evaluation Matrix

Each query’s results were manually assessed using the following relevance scale:

- `0` = Not relevant  
- `1` = Somewhat relevant  
- `2` = Highly relevant

The table below captures all relevant information for each query/system combination:

| Query ID | Query Text  | Filters Applied | System Version | Rank | Result Title  | Relevance (0–2)  | Reciprocal Rank  | Log2(Rank+1)   | DCG Contribution   |
|:--------:|:------------|:----------------|:---------------|:----:|:--------------|:----------------:|:----------------:|:--------------:|:------------------:|
| Q#       | RATE        | n/a             | Old            | 1    | ...           |                  |                  |                |                    |
| Q#       | RATE        | Wearables       | Old            | 1    | ...           |                  |                  |                |                    |
| Q#       | Wearables   | n/a             | Old            | 2    | ...           |                  |                  |                |                    |
| Q#       | n/a         | Wearables       | Old            | 1    | ...           |                  |                  |                |                    |
| Q#       | RATE        | n/a             | Old            | 1    | ...           |                  |                  |                |                    |
| Q#       | RATE        | n/a             | Old            | 1    | ...           |                  |                  |                |                    |
| Q#       | RATE        | n/a             | Old            | 1    | ...           |                  |                  |                |                    |
| Q#       | RATE        | n/a             | Old            | 1    | ...           |                  |                  |                |                    |
| Q#       | RATE        | n/a             | Old            | 1    | ...           |                  |                  |                |                    |
| Q#       | RATE        | n/a             | Old            | 1    | ...           |                  |                  |                |                    |
| Q#       | RATE        | n/a             | Old            | 1    | ...           |                  |                  |                |                    |

---

## 4. Evaluation Protocol

The following steps were used to ensure consistency in the evaluation:

1. A set of 5–10 representative user queries were defined in advance.
2. Top 5 results for each query were captured from both systems.
3. Relevance judgments were made based on domain knowledge.
4. Calculations for each metric (P@5, MRR, nDCG@5) were computed using the scoring matrix.

---

## 5. Limitations

- **Single-evaluator bias:** This evaluation reflects the judgment of one domain expert, which may introduce subjectivity.
- **Limited query set:** A small number of test queries were used, limiting generalizability.
- **Offline testing only:** Results were not validated with real users in live sessions or A/B tests.
- **Search behavior context omitted:** The evaluation does not account for time to result, scrolling, or click behavior.

Despite these limitations, the evaluation provides a **directionally useful** analysis of relative system performance.

---

## 6. Recommendations

Based on metric results and qualitative observations:

- If the vector search consistently outperforms in MRR and nDCG@5, consider prioritizing its rollout.
- Use the results to guide **further user testing or A/B testing** with live users.
- Explore ways to blend keyword and semantic search if some queries perform better in one engine than the other.
- Continue refining query processing and metadata quality, as both impact performance.

---

## 7. Appendix

- [Link to full data table (Excel)](./Search_Evaluation_Template.xlsx)
- [Markdown version of scoring matrix](./search_scoring_matrix.md)

---

## 8. References

### Precision@5
*Of the top X results, how many were actually relevant — higher is better.*

- **What it measures?**  
  - The proportion of relevant items in the top *k* results by the search engine.
  - *K is defined as the entire catalog on AGENT (env) due to a small search catalog.*

- **Why it's recommended?**  
  - It's simple, intuitive, and reflects what users see first (typically only the top 5-10 results) 
  - Strongly aligned with real-world behavior: users rarely go beyond the first page of results 
  - Useful for comparing how well two systems prioritize relevant results early in the ranking 

- **Sources**
  - [1] Manning, R., Raghavan, P., & Schütze, H. (2008). *Introduction to Information Retrieval. Cambridge University Press.*
  - [2] Sakai, T. (2007). *On the Reliability of Information Retrieval Metrics.*,

&nbsp;

### Mean Reciprocal Rank (MRR)
*How early does the first relevant result appear in the list — the sooner, the better, so higher is better.*

- **What it measures?**
  - The inverse of the rank at which the first relevant result appears, averaged across queries

$$ 
MRR = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \frac{1}{rank_i}
$$

- **Why it's recommended?**
  - Especially effective for navigational queries (where the user is looking for a specific item)
  - Rewards systems that return at least one relevant result early in the list
  - Often used in QA systems and internal search where finding one "correct" thing is the goal

- **Sources**
  - [3] Voorhees, E. M. (1999). *The TREC-8 Question Answering Track Evaluation.*
  - [4] Manning et al. (2008) — *Introduction to IR, Chapter 8*

&nbsp;

### NDCG@k (Normalized Discounted Cumulative Gain)
*How well are the most relevant results ranked near the top — higher is better, with a perfect score being 1.*

- **What it measures?**
  - A graded relevance score that penalizes relevant results that appear lower in the ranking
  - Supports multi-level relevance judgments (e.g., hihgly relevant vs. somewhat relevant)

$$
DCG@k = rel_1 + \sum_{i=2}^k \frac{rel_i}{\log_2(i + 1)}
$$

- **Why it's recommended?**
  - Captures ranking quality more holistically than binary metrics
  - Suitable when some items are more relevant than others — especially common in serach catalogs like ours
  - De factor standard for graded relevance in search engines, recommendation systems, and ML benchmarks

- **Sources**
  - [5] Järvelin, K., & Kekäläinen, J. (2002). *Cumulated gain-based evaluation of IR techniques. ACM TOIS.*
  - [6] Microsoft Research (2008). *Learning to Rank Challenge.*
  - [7] Manning et al. (2008), *Chapter 8.4*



&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;
---

## pLayGrouNd
| Method | What it measures? | Why it's recommended? | Sources |
|:------:|:------------------|:----------------------|:--------|
| Precision@5 | The proportion of relevant items in the top *k* results by the search engine. *k is defined as the entire catalog on AGENT (env?) due to a small search catalog* | It's simple, intuitive, and reflects what users see first (typically only the top 5-10 results). Strongly aligned with real-world behavior: users rarely go beyond the first page of results. Useful for comparing how well two systems priortize reelvant results early in the ranking. | [1] Manning, R., Raghavan, P., & Schütze, H. (2008). *Introduction to Information Retrieval. Cambridge University Press.* [2] Sakai, T. (2007). *On the Reliability of Information Retrieval Metrics.* |

| Query ID | Query Text       | Source             |
|:--------:|:-----------------|:-------------------|
| Q1       | search example   | AWS Cloudwatch Log |
| Q2       | search example   | AWS Cloudwatch Log |
| Q3       | search example   | AWS Cloudwatch Log |
| Q4       | search example   | AWS Cloudwatch Log |
| Q5       | search example   | AWS Cloudwatch Log |
| Q6       | search example   | AWS Cloudwatch Log |
| Q7       | search example   | AWS Cloudwatch Log |
| Q8       | search example   | AWS Cloudwatch Log |
| Q9       | search example   | AWS Cloudwatch Log |
| Q10      | search example   | AWS Cloudwatch Log |


