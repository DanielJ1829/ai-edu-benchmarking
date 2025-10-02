import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#--- Load your data ---

df = pd.read_csv("responsedata.csv")
pd.set_option('display.colheader_justify', 'left')

#Overall Stats By Model:
overall_stats = df.groupby("model")["total_score"].agg(mean="mean",median="median",std="std",min="min",max="max")
overall_stats["cv"] = overall_stats["std"] / overall_stats["mean"] #coefficient of variation (CV)
print("\nOverall stats by model:\n",overall_stats) #display statistics

#Plot means for each model, with std as error bars
fig = go.Figure()
fig.add_trace(go.Bar(x=overall_stats.index, y=overall_stats["mean"],
                     error_y=dict(type='data',array=overall_stats["std"],visible=True),name="Mean ± Std"))
fig.add_trace(go.Scatter(x=overall_stats.index,y=overall_stats["cv"], mode="markers+lines",name="CV (σ/mean)",yaxis="y2"))
#Addding CV as a scatter plot on top ^
fig.update_layout(title="Overall Model Performance",yaxis=dict(title="Mean Total Score"),
                  yaxis2=dict(title="Coefficient of Variation", overlaying="y", side="right")) #Dual y-axis for CV
fig.show()

#Overall Stats By Question:
overall_stats_q = df.groupby("question_id")["total_score"].agg(mean="mean",median="median",std="std",min="min",max="max")
overall_stats_q["cv"] = overall_stats_q["std"] / overall_stats_q["mean"] #coefficient of variation (CV)
print("\nOverall stats by question:\n"," ", overall_stats_q) #display statistics


#Overall Stats By Persona
overall_stats_p = df.groupby("persona")["total_score"].agg(mean="mean",median="median",std="std",min="min",max="max")
overall_stats_p["cv"] = overall_stats_p["std"] / overall_stats_p["mean"] #coefficient of variation (CV)
print("\nOverall stats by persona:\n"," ", overall_stats_p) #display statistics



#general stats by model and persona:
subset = df[df["question_id"]==5]
persona_stats = df.groupby(["persona", "model"])["total_score"].agg(mean="mean",std="std",skew=pd.Series.skew,
                                                                    kurt=pd.Series.kurtosis)
persona_stats["cv"] = persona_stats["std"] / persona_stats["mean"]
print("\nBy model & persona:\n", persona_stats) #display results

#data + text matrices to overlay onto heatmaps for model/persona analysis
mean_matrix, std_matrix = persona_stats["mean"].unstack(), persona_stats["std"].unstack()
text_matrix = ("μ=" + mean_matrix.round(2).astype(str) +
               " (σ=" + std_matrix.round(2).astype(str) + ")")

#Heatmap - model vs persona
heatmap = px.imshow(mean_matrix, color_continuous_scale="RdYlGn", zmin=0, zmax=10,
                    labels=dict(x="Model", y="Persona", color="Mean Score"), text_auto=False,
                    title="Mean Score by Persona x Model")
heatmap.update_traces(text=text_matrix.values, texttemplate="%{text}",textfont_size=10)
heatmap.add_scatter(x=[None], y=[None], mode="markers", marker=dict(size=0, color="rgba(0,0,0,0)"),
                    name="μ = mean, σ = std")
heatmap.show()

#By question:

#General stats by question
question_stats = df.groupby(["question_id", "model"])["total_score"].agg(mean="mean",std="std")
print("\nBy model & question:\n", question_stats)

#data and text matrices for model/question analysis
mean_matrix_q, std_matrix_q = question_stats["mean"].unstack(), question_stats["std"].unstack()
text_matrix_q = ("μ=" + mean_matrix_q.round(2).astype(str) + " (σ=" + std_matrix_q.round(2).astype(str) + ")")

#Heatmap - model vs question
q_heatmap = px.imshow(mean_matrix_q, color_continuous_scale="RdYlGn", zmin=0, zmax=10,
                      labels=dict(x="Model", y="Question", color="Mean Score"),text_auto=False,
                      title="Mean Score by Question x Model")
q_heatmap.update_traces(text=text_matrix_q.values, texttemplate="%{text}", textfont_size=10)
q_heatmap.add_scatter(x=[None], y=[None], mode="markers", marker=dict(size=0, color="rgba(0,0,0,0)"),
                      name="μ = mean, σ = std")
q_heatmap.show()


#By persona and question (averaging over models) - denote persona&question as pq in code:
pq_stats = df.groupby(["question_id", "persona"])["total_score"].agg(mean="mean",std="std",skew=pd.Series.skew)
pq_stats["cv"] = pq_stats["std"] / pq_stats["mean"]
print("\nBy persona & question - Cross-Model Analysis:\n", pq_stats) #display results

#data + text matrices to overlay onto heatmaps for model/persona analysis
mean_matrix_pq, std_matrix_pq = pq_stats["mean"].unstack(), pq_stats["std"].unstack()
text_matrix_pq = ("μ=" + mean_matrix_pq.round(2).astype(str) +
               " (σ=" + std_matrix_pq.round(2).astype(str) + ")")

#Heatmap - question vs persona
heatmap_pq = px.imshow(mean_matrix_pq, color_continuous_scale="RdYlGn", zmin=0, zmax=10,
                    labels=dict(x="Persona", y="Question", color="Mean Score"), text_auto=False,
                    title="Mean Score by Question x Persona")
heatmap_pq.update_traces(text=text_matrix_pq.values, texttemplate="%{text}",textfont_size=10)
heatmap_pq.add_scatter(x=[None], y=[None], mode="markers", marker=dict(size=0, color="rgba(0,0,0,0)"),
                    name="μ = mean, σ = std")
heatmap_pq.update_layout(width=1200, height=700,autosize=False, xaxis_constrain='domain', yaxis_constrain='domain')

heatmap_pq.show()


#worst performer: question 5 (analysis)
subset = df[df["question_id"]==5]
q5_stats = subset.groupby(["persona", "model"])["total_score"].agg(mean="mean")

table = q5_stats["mean"].unstack()  # rows=persona, cols=model
table["persona mean"] = table.mean(axis=1) # Add persona means (row means)
table.loc["model mean"] = table.mean(axis=0) # Add model means (column means)
print("\nBy persona & model - Question 5:\n",table)

#Heatmap - model vs persona
heatmap_q5 = px.imshow(q5_stats["mean"].unstack(), color_continuous_scale="RdYlGn", zmin=0, zmax=10,
                    labels=dict(x="Model", y="Persona", color="Score"), text_auto=True,
                    title="Score by Persona x Model (Question 5)")
heatmap_q5.show()

#By metric
metrics = ["correctness", "completeness", "clarity", "educational_value", "tone"]
metric_stats = df.groupby("model")[metrics].mean()
print("\nBy metric:\n", metric_stats)

#radar plot (one polygon per model)
radar = go.Figure()
for model in metric_stats.index:
    radar.add_trace(go.Scatterpolar(r=metric_stats.loc[model].values,theta=metric_stats.columns,
                                    fill="toself",name=model))
    radar.update_layout(title="Metric Breakdown by Model", polar=dict(radialaxis=dict(visible=True, range=[0, 2])))
radar.show()
