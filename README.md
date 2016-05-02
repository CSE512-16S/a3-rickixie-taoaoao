a3-rickixie-taoaoao
===============

## Team Members

1. Ricki Si Xie (rickixie)
2. Yitao Wang (yitaow)

## World Bank Gender Data Explorer 

![Thumbnail](thumbnail.gif)

A visualization of the [World Bank Gender Statistics data] (http://datatopics.worldbank.org/gender/home).

In this interactive visualization, we wanted to explore the relationship between gender and opportunity. The visualization includes data from the World Bank Gender Statistics, which includes time-based parameters of different indicators. The visualization was inspired by [New York Time’s tax report in 2012] (http://www.nytimes.com/interactive/2012/11/30/us/tax-burden.html).

We used small multiples to show the change in data while allow direct comparison across different income levels. As seen in the visualization, indicators are presented in rows, while the columns are aggregated with the income levels of all countries. Additionally, both male and female value were plot in the same multiples to represent the disparity. To see the value of different gender difference indicators You can hover over the each graph to view the actual value of each year. 

(Put your a brief description of your final interactive visualization application and your dataset here.)


## Running Instructions

Put your running instructions here. (Tell us how to run your visualization.)

If your visualization is web-based,  it would be great if your submission can be opened online. [Github Pages](http://pages.github.com/) is a good and easy way to put your visualization online so you can put your link here.  For example:

Access our visualization at http://cse512-16s.github.io/a3-jheer-mcorrell-jhoffs/ or download this repository and run `python -m SimpleHTTPServer 9000` and access this from http://localhost:9000/.

If you put your work online, please also write a [one-line description and add a link to your final work](http://note.io/1n3u46s) so people can access it directly from the CSE512-16S page.

## Story Board

Put either your storyboard content or a [link to your storyboard pdf file](storyboard.pdf?raw=true) here. Just like A2, you can use any software to create a *reasonable* pdf storyboard.

Since there are multiple dimensions in the gender statistics, we thought small multiples will be an ideal representation of our dataset. To allow comparison, we also wanted to have a tooltip that show the value of a indicator across all different levels while the audiences hover over a particular year.

![storyboard2](storyboard/storyboard2.jpg)

Similarity, we were also envisioned to have some form of filtering and sorting  to reorder the graphs to show the overall trends. We were also thinking using view manipulation where the audience can click on specific multiple and it will transition to another page that shows all the countries that belongs to the same income levels. 

![storyboard1](storyboard/storyboard1.png)

We also wanted to have some curations in the data that we represented to create meaning caption for the visualization. For example, we wanted to have a subsection in the education section that includes key indicators that represent education opportunity of women and young girls, and another section for the economic and political participation of these population. 
![storyboard3](storyboard/storyboard3.jpg)

We also prototyped our design with Tableau as shown below.

![storyboard4](storyboard/storyboard4.png)

### Changes between Storyboard and the Final Implementation

A paragraph explaining changes between the storyboard and the final implementation.
####Design Decision
We utilized the [ColorBrewer](http://colorbrewer2.org/) tool to choose our color encoding of the gender data.


## Development Process

Include:
- Breakdown of how the work was split among the group members.
  - **Ricki** worked on gathering data using the World Bank API and transform it for the visualization using python and d3, she also contributed to the styling and creating layout of the small multiples
  - **Taotao** created the multi-series visualization of the data, she also contributed to the ideation and storyboarding of the interactions

- A commentary on the development process, including answers to the following questions:
  - Roughly how much time did you spend developing your application?
    - Research and finalized the data sets: The whole week…
    - Processed and retrieving the data from world bank: 1 day (included learning python)
    - Building the data visulization: ???? days..
  - What aspects took the most time?
    - Both of us had no prior experience with d3.js and limited experience with javascript, so learning about d3 with the formatted the data took is the most time. We may also scale up the challenges than what we can do in the time that allowed. 

