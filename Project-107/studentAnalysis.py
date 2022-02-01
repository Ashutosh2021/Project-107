import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

#studentDf = df.groupby("student_id")["attempt"].mean()
studentDf = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()

print(studentDf)


fig = px.scatter(data_frame = studentDf , x =  "student_id", y ="level",color="attempt",size="attempt")
fig.show()