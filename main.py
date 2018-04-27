import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import mysql.connector
from datetime import datetime as dt
import statistics
cnx = mysql.connector.connect(user='student', password='cs336student',
                              host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              database='CryptoNews')
							  
#query = "select M.currency_name, (100*((N.quote-M.quote)/M.quote)) as ch from (select A.currency_name,A.quote from Value A JOIN (select currency_name, min(time) as time from Value where time LIKE '2018-03-24%' group by currency_name) B on A.currency_name=B.currency_name and A.time = B.time) M JOIN (select X.currency_name,X.quote from Value X JOIN (select currency_name, max(time) as time from Value where time LIKE '2018-03-24%' group by currency_name) Y on X.currency_name=Y.currency_name and X.time = Y.time) N on M.currency_name=N.currency_name group by currency_name order by ch DESC"							  
#dm = DataManager('./vgsales.csv')
col = "a"
#dm = pd.read_sql(query,cnx);

#print(dm.iloc[:,0])

#date
#dm 

x1=[]
y1=[]
#x2=[]
#y2=[]

#generate_graph() generates the graph based on the dropdown input 
def generate_graph(dropdown):
	if(dropdown=='g'):
		#dm.reset_data()
		#dm.group_sales_by(column_name="Year")
		#global dm
		#x1 = dm.iloc[:20,0].tolist()
		#x2 = dm.iloc[:20,1].tolist()
		
		z1=x1[:30]
		z2=y1[:30]
		
		#print(x1[1])
		#print(y1[1])
		x = dcc.Graph(
			id='loss',
			figure={
				'data': [
					{'x': z1 , 'y': z2, 'type': 'bar'},
					#{'x': dm.data.iloc[:,0] , 'y': dm.data.iloc[:,1], 'type': 'line', 'name': 'North America','mode':'lines+markers'},
					#{'x': dm.data.iloc[:,0] , 'y': dm.data.iloc[:,2], 'type': 'line', 'name': 'Europe','mode':'lines+markers'},
					#{'x': dm.data.iloc[:,0] , 'y': dm.data.iloc[:,3], 'type': 'line', 'name': 'Japan','mode':'lines+markers'},
					#{'x': dm.data.iloc[:,0] , 'y': dm.data.iloc[:,4], 'type': 'line', 'name': 'Other','mode':'lines+markers'},
					
				],
				'layout': {
					'title': 'Top Gainers',
					'xaxis' : {'title':'Currency'},
					'yaxis' : {'title':'Gain in %'},
					'plot_bgcolor': '#eeeeee',
					'paper_bgcolor': '#eeeeee',
				}
			}
		)
		
		return x

	elif(dropdown=='l'):
		#dm.reset_data()
		#dm.group_sales_by(column_name="Year")
		#global dm
		#x1 = dm.iloc[:20,0].tolist()
		#x2 = dm.iloc[:20,1].tolist()
		
		z1=x1[-30:]
		z2=y1[-30:]
		
		#print(x1[1])
		#print(y1[1])
		x = dcc.Graph(
			id='gains',
			figure={
				'data': [
					{'x': z1 , 'y': z2, 'type': 'bar'},
					#{'x': dm.data.iloc[:,0] , 'y': dm.data.iloc[:,1], 'type': 'line', 'name': 'North America','mode':'lines+markers'},
					#{'x': dm.data.iloc[:,0] , 'y': dm.data.iloc[:,2], 'type': 'line', 'name': 'Europe','mode':'lines+markers'},
					#{'x': dm.data.iloc[:,0] , 'y': dm.data.iloc[:,3], 'type': 'line', 'name': 'Japan','mode':'lines+markers'},
					#{'x': dm.data.iloc[:,0] , 'y': dm.data.iloc[:,4], 'type': 'line', 'name': 'Other','mode':'lines+markers'},
					
				],
				'layout': {
					'title': 'Top Gainers',
					'xaxis' : {'title':'Currency'},
					'yaxis' : {'title':'Loss in %'},
					'plot_bgcolor': '#eeeeee',
					'paper_bgcolor': '#eeeeee',
				}
			}
		)
		
		return x		
	
	elif(dropdown=='p'):
		z1=x1[:10]
		z2=y1[:10]
		x = dcc.Dropdown(
			id='plot1',
			options=[{'label':z1[0], 'value':z1[0]},
			{'label':z1[1], 'value':z1[1]},
			{'label':z1[2], 'value':z1[2]},
			{'label':z1[3], 'value':z1[3]},
			{'label':z1[4], 'value':z1[4]},
			{'label':z1[5], 'value':z1[5]},
			{'label':z1[6], 'value':z1[6]},
			{'label':z1[7], 'value':z1[7]},
			{'label':z1[8], 'value':z1[8]},
			{'label':z1[9], 'value':z1[9]}],
			value = z1[0],
			), html.Div(style={'width':'100%'} , id='piec')
		return x
	
	elif(dropdown=='d'):
		z1=x1[-10:]
		z2=y1[-10:]
		x = dcc.Dropdown(
			id='plot1',
			options=[{'label':z1[-1], 'value':z1[-1]},
			{'label':z1[-2], 'value':z1[-2]},
			{'label':z1[-3], 'value':z1[-3]},
			{'label':z1[-4], 'value':z1[-4]},
			{'label':z1[-5], 'value':z1[-5]},
			{'label':z1[-6], 'value':z1[-6]},
			{'label':z1[-7], 'value':z1[-7]},
			{'label':z1[-8], 'value':z1[-8]},
			{'label':z1[-9], 'value':z1[-9]}],
			value = z1[-1],
			), html.Div(style={'width':'100%'} , id='piec')
		return x

#generate_pie() generates a pie chart based on the different tabs 		
def generate_pie(crypto):
		#hist = []
		hist=pd.read_sql("select quote, time from CryptoNews.Value where currency_name like '"+crypto+"' and time < '"+d+"'",cnx)
		now=pd.read_sql("select quote,time from CryptoNews.Value where currency_name like '"+crypto+"' and time > '"+d+"' and time < '"+e+" 23:59:59'",cnx)
		
		h = hist.iloc[:,0].tolist()
		std = statistics.stdev(h)
		m = statistics.mean(h)
		fhp ="YES"
		if std>m:
			fhp ="NO"
		
		date1 = dt(int(d[:4]),int(d[5:7]),int(d[8:]))
		date = date1
		date2 = dt(int(e[:4]),int(e[5:7]),int(e[8:]))
		
		diff1 = date1-dt(2018,2,19)
		diff2 = date2-date1
		
		#print(27/diff1.days)
		
		day=[]
		td = dt(2018,3,24)-dt(2018,3,23)
		while date <= date2:
			day.append(date.isoformat()[:10])
			date=date+td
		
		#print(day)
		temp=[]
		for i in day:
			pump = pd.read_sql("select M.currency_name, (100*((N.quote-M.quote)/M.quote)) as ch from (select A.currency_name,A.quote from Value A JOIN (select currency_name, min(time) as time from Value where time LIKE '"+i+"%' group by currency_name) B on A.currency_name=B.currency_name and A.time = B.time) M JOIN (select X.currency_name,X.quote from Value X JOIN (select currency_name, max(time) as time from Value where time LIKE '"+i+"%' group by currency_name) Y on X.currency_name=Y.currency_name and X.time = Y.time) N on M.currency_name=N.currency_name where M.currency_name like '"+crypto+"' group by currency_name order by ch DESC",cnx)
			if s=='p':
				if pump.iloc[:,1].tolist()[0] > 100:
					temp.append(i)
			elif s=='d':
				if pump.iloc[:,1].tolist()[0] < -50:
					temp.append(i)
		x = now.iloc[:,1].tolist()
		y = now.iloc[:,0].tolist()
		
		
		
		if len(temp)==0:
			temp.append("No date with a sudden increase/decrease. Possibally not a pump/dump.")
		
		c1 = pd.read_sql("select count(*) from CryptoNews.cryptonews where content like '%"+crypto+"%' and date < '"+d+"'",cnx)
		c2 = pd.read_sql("select count(*) from CryptoNews.cryptonews where content like '%"+crypto+"%' and date > '"+d+"' and date < '"+e+"'",cnx)
		
		return html.Div(children=[dcc.Graph(
				id='pi',
				figure={
					'data': [
						{'x': x , 'y': y, 'type': 'line', 'name': 'Global','mode':'lines+markers'},
					],
					'layout': {
						'title': crypto+' price',
						'plot_bgcolor': '#eeeeee',
						'paper_bgcolor': '#eeeeee',
					}
				}
			),
			html.Div(children="Standard deviation of historical values is "+str(std)+". Mean of the historical values is "+str(m)),
			html.Div(children="Flat Historical Prices: "+fhp), 
			html.Div(children="Sudden increase/decrease of currecny on :"+temp[0]),
			html.Div(children="Articles talking about "+crypto+" before "+d+": "+str((c1.iloc[:,0].tolist()[0])/diff1.days)),
			html.Div(children="Articles talking about "+crypto+" between "+d+" and "+e+": "+str((c2.iloc[:,0].tolist()[0])/diff2.days)),
			])
		
#initialize application
app = dash.Dash()
server = app.server
app.config['suppress_callback_exceptions']=True

#application layout
app.layout = html.Div(style={'backgroundImage':'url("http://www.designbolts.com/wp-content/uploads/2013/02/Golf-Shirt-Grey-Seamless-Pattern-For-Website-Background.jpg")','borderRadius':'10px','min-height':'95vh'},children=[
    html.H1(style={'textAlign':'center','font':'bold 30px Castellar, serif','padding':'20px 0px 0px 0px'} ,children='Crypto Analysis'),

	html.Label(style={'margin': '0% 0% 0% 2.5%','font':'20px Britannic, serif'},children='Select a date:'),
	
	html.Div(style={'margin':'0% 0% 0% 2.5%'},children=dcc.DatePickerRange(
		id='range',
		start_date=dt(2018,3,18),
		end_date=dt(2018,3,24)
		#number_of_months_shown = 1,
		
	
	)),
	
	#html.Input(type='date'),
	
	html.Div(id='seldate',style={'display':'none'}),
	html.Div(style={'margin': '0% 0% 0% 2.5%' },children=dcc.Dropdown(
		id='graphs',
		options=[{'label':'Top Gainers', 'value':'g',},{'label':'Top Losers', 'value':'l'},{'label':'Possible Pumps', 'value':'p',},{'label':'Possible Dumps', 'value':'d'}],
		value = 'g'
	)),
	html.Div(style={'width':'95%','margin':'1% 2.5% 1% 2.5%','borderRadius':'10px','opacity':'1'}, children=html.Div(id='output')),
	
	

])


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('range', 'start_date'),dash.dependencies.Input('range','end_date'),dash.dependencies.Input('graphs','value')])
	
def update_output(value,value2,graph):
	global d
	d = '{}'.format(value)
	global e
	e = '{}'.format(value2)
	global query
	query = "select M.currency_name, (100*((N.quote-M.quote)/M.quote)) as ch from (select A.currency_name,A.quote from Value A JOIN (select currency_name, min(time) as time from Value where time LIKE '"+d+"%' group by currency_name) B on A.currency_name=B.currency_name and A.time = B.time) M JOIN (select X.currency_name,X.quote from Value X JOIN (select currency_name, max(time) as time from Value where time LIKE '"+e+"%' group by currency_name) Y on X.currency_name=Y.currency_name and X.time = Y.time) N on M.currency_name=N.currency_name group by currency_name order by ch DESC"
	global dm
	dm = pd.read_sql(query,cnx)
	global x1
	x1=dm.iloc[:,0].tolist()
	global y1
	y1=dm.iloc[:,1].tolist()
	#print(x1)
	#print(y1)
	global s
	s = '{}'.format(graph)
	return generate_graph(s)
	#return d
	#return generate_graph(s)

'''
#callback for dropdown for different plots 
@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('graphs', 'value')])
	
def update_output(value):
	s = '{}'.format(value)
	return generate_graph(s)
'''	
#callback for different tabs for different pie charts
@app.callback(
    dash.dependencies.Output('piec', 'children'),
    [dash.dependencies.Input('plot1', 'value')])
	
def update_output(value):
	#global col
	#col = '{}'.format(value)
	return generate_pie(value)

# Dash CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# Loading screen CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})
	
if __name__ == '__main__':
    app.run_server(debug=True)
