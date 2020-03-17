''' Using Spearman's dendrogram to show if there are two variables are of the same effect. Closer the variables are in the end nodes, 
higher the correlation they have. 
Spearman's R square: use rank instead of level of data. This avoids the problem with quadratic pattern. 
'''

'''Always do one hot encoding with categorical varibales(with less than 7 types). 
You may find some type in a variable extremely correlated with y.
'''

'''Get a calsual relationship
if we draw a naive plot of price and year, it includes other issues that affects price. So we can't say the year causes the price.
We can use pdp graph to fix other variables constant and conclude a calsual relationship. Such as 'if we sell the same bulldozer to the same person.... in differetn years, the price flucutations.
'''
