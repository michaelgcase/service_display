import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.DASH(__name__)
df = pd.DataFrame({
	"Fruit" : ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
	"Amount" : [4, 1, 2, 2, 4, 5],
	"City" : ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmore="group")
app.layout = html.Div(children=[
	html.H1(children="Hello Dash"),

	html.Div(children='''
		Dash: A web application framework for you data
	'''),

	dcc.Graph(
		id='example-graph',
		figure=fig
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)



