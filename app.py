######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
distributors=['Paramount', 'Disney', 'Warner Bros', 'Universal', 'Sony']
dist_movies=[3, 3, 1, 2, 1]
color='blue'
mytitle='Highest grossing movies of 2022'

label='Distributor'
label2='# of movies'

########### Set up the chart

def make_that_cool_barchart(distributors, dist_movies, color, label, label2, mytitle):
    dist = go.Bar(
        x=distributors,
        y=dist_movies,
        name=label,
        marker={'color':color},
    )


    movie_fig = go.Figure(data=dist)
    movie_fig.update_layout(title_text=mytitle)
    movie_fig.update_xaxes(title_text=label)
    movie_fig.update_yaxes(title_text=label2)
    return movie_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(distributors, dist_movies, color, label, label2, mytitle)
    fig.write_html('docs/barchart.html')
    print('We successfully updated the barchart!')
