### Plan
Goal is to remove date outliers

#### Method

I indentified any day isolated by both sides by 7 days as an outlier and removed all the data, there were 161 outliers found with this method that was removed
There was also a method created to in order to remove rows with temperature outliers (1.5 x IQR +- 25% or 75%) but as we're trying to find an anomaly, I decided to keep that off.
