This repository contains a benchmarking project that evaluates the performance of multiple large language models (LLMs) — Claude, DeepSeek, and GPT-5 — when answering a fixed set of math/physics problems across different student personas.

The goal is to measure not only correctness, but also how clear, complete, educational, and supportive each model’s responses are, with a focus on how well they would assist real learners.

--------------------
**Repository Structure**

ai-edu-benchmarking/            # Root Folder
├── data/                       # Inputs for benchmarking
│   ├── Personas - Prompts/     # Persona descriptions + prompts for each persona&question
│   ├── Questions/              # Benchmark questions (Markdown + Jupyter) - General questions and expected solutions
│   ├── Responses/              # Raw model responses and response data
│   └── EvaluationRubric.md     # The evaluation rubric to grade responses + markdown/LaTeX notes for annotation
│
├── Analysis/                   
│   ├── Annotated Responses/    # Manual annotations with rubric applied
│   ├── DataAnalysis/           # Python code and results for statistical analysis
│       ├── Graphics/           # Generated plots/heatmaps
│       ├── MainAnalysis.py     # Analysis pipeline (pandas + plotly) - produces dashbooards when run
│       └── responsedata.csv    # Processed dataset (scores + notes)
│
├── README.md                   # Project documentation
└── Summary.md                  # A brief analysis of the results

-------------------
**Personas**
The benchmark defines five student personas (in data/Personas - Prompts/), reflecting different levels (we define learning levels 1, 2 and 3 dependent on the persona) of background knowledge and learning needs (from novice to advanced).
This allows evaluation not just of factual accuracy/reasoning ability, but of how well the models adapt their explanations to different learner profiles.

-----------------
**Benchmarking Questions**
The questions (in data/Questions/) cover a mix of:
1.) Mathematics (integration, algebra, probability, geometry)

2.) Physics (projectile motion, kinematics, mechanics, electricity)

Each model was asked the same set of questions, under each persona prompt, to simulate tutoring scenarios.

------------------
**Evaluation Rubric**

Each response was graded along five dimensions (0–2 scale):

1.) Correctness — Is the bottom-line answer correct?

2.) Completeness — Does the response address the full scope of the question?

3.) Clarity — Is the reasoning easy to follow?

4.) Educational Value — Does it provide transferable insights for learning?

5.) Tone/Coherence — Is the tone supportive and consistent?

A total score out of 10 was calculated for each response.
(See data/EvaluationRubric.md for full details.)

-------------------------
**Data Analysis**
The analysis (in Analysis/DataAnalysis/) was carried out using pandas and plotly, and includes:
Overall Model Performance:
Mean, median, min, max, standard deviation, coefficient of variation (CV).

By Persona:
Mean & std for each model × persona, plus skewness/kurtosis where relevant.

By Question:
Average scores to identify the “hardest” questions across models/personas.

Question 5 focus:
An analysis of how models did specifically on question 5 since this was the weakest performing question and saw the largest standard deviations across models

By Metric:
Breakdown of how models perform on correctness vs. clarity vs. tone, etc.

Visualizations include heatmaps, bar charts, and tables (see Analysis/DataAnalysis/Graphics/).
A summary of the analysis can be seen in /Summary.md



--------------------------
**How to Run the Analysis**

1) Clone the repo:
*git clone https://github.com/yourusername/ai-edu-benchmarking.git*
*cd ai-edu-benchmarking/Analysis/DataAnalysis* <--although in practice, just ensure you responsedata.csv and MainAnalysis.py are in the same directory-->

2) Install dependencies (recommended in a virtualenv):
*pip install pandas plotly*

3) Run the analysis script:
*python MainAnalysis.py*

4) Results:
Tables saved in Results Table.txt
Visualizations saved in Graphics/

