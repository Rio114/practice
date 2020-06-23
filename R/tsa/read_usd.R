num <- 1000
usd <- tail(read.csv('data/USDJPY.txt'), num)
y_usd <- ts(data=usd$X.CLOSE)