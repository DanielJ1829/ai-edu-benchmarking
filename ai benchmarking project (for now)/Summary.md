# Results Summary

This benchmarking study compared the performance of *Claude*, *DeepSeek*, and *GPT-5* across *five learner personas* and *six assessment questions*, with each question grades by *learning level*. Responses were graded on *Correctness, Completeness, Clarity, Educational Value, and Tone*, with scores aggregated into a total out of 10.

---

## Overall Model Performance

| Model    | Mean | Median | Std Dev | Min | Max | CV   |
| -------- | ---- | ------ | ------- | --- | --- | ---- |
| Claude   | 5.97 | 7.0    | 2.37    | 2   | 10  | 0.40 |
| DeepSeek | 6.90 | 7.0    | 2.31    | 1   | 10  | 0.33 |
| GPT-5    | 8.27 | 9.0    | 1.53    | 5   | 10  | 0.19 |

* *GPT-5* consistently outperformed the others, with the *highest mean (8.27)** and **lowest variability (CV = 0.19)*.
* *Claude* trailed, with lower average scores and higher spread.
* *DeepSeek* performed in between, with greater volatility than GPT-5 but higher mean than Claude.

---

## Performance by Question

| Q | Mean | Std Dev | Notes                                                         |
| - | ---- | ------- | ------------------------------------------------------------- |
| 1 | 7.0  | 1.73    | Balanced performance across models.                           |
| 2 | 6.93 | 2.31    | Higher variance; GPT-5 dominates.                             |
| 3 | 7.0  | 1.93    | Consistent across models, moderate spread.                    |
| 4 | 8.13 | 1.64    | Strongest overall performance.                                |
| 5 | 4.87 | 2.92    | **Most difficult question**; large variability across models. |
| 6 | 8.33 | 1.35    | High and stable performance.                                  |

* *Question 5* stands out as the hardest, with the **lowest mean (4.87)** and the **highest relative variability (CV = 0.60)**.
* *Question 6* was the most consistently well-answered.

---

## Performance by Persona

| Persona | Mean | Std Dev | Notes                                |
| ------- | ---- | ------- | ------------------------------------ |
| P1      | 6.89 | 2.32    | Middle-range scores.                 |
| P2      | 6.72 | 2.63    | Slightly weaker performance.         |
| P3      | 7.22 | 2.44    | Stronger, but high variability.      |
| P4      | 7.39 | 2.33    | **Best performing persona overall**. |
| P5      | 7.0  | 1.85    | Stable and solid performance.        |

* *Persona 4* elicited the strongest responses across models.
* *Persona 2* was more challenging, with lower means and higher variability.

---

## Breakdown by Metric

| Model    | Correctness | Completeness | Clarity | Educational Value | Tone |
| -------- | ----------- | ------------ | ------- | ----------------- | ---- |
| Claude   | 1.30        | 1.33         | 1.30    | 0.87              | 1.20 |
| DeepSeek | 1.70        | 1.37         | 1.27    | 1.27              | 1.37 |
| GPT-5    | 1.97        | 1.70         | 1.60    | 1.40              | 1.60 |

* *GPT-5* leads across all metrics, especially in *Correctness* and *Clarity*.
* *Claude* struggles with **Educational Value**, averaging below 1.
* *DeepSeek* achieves moderate balance, but lags in clarity.

---

## Key Insights

1. *GPT-5* is the most reliable and accurate model, both in overall averages and in per-persona/per-question breakdowns.
2. *Claude* is inconsistent, with relatively high variability and weaker educational value.
3. *DeepSeek* shows moderate strength but occasionally struggles, especially on challenging questions.
4. *Question 5* consistently challenged all models, suggesting it was the benchmark’s most discriminating item.
5. Personas 2 and 3 yielded more variable responses, while Persona 4 consistently received stronger answers.

---

## Other Notes
1. The rubric was designed in such a way where poor resposnses occasionally lacked distinction with better responses, leading to lower ranges in model performances than predicted. A better defined rubric would have prevented this issue and would've allowed for more consistent results.