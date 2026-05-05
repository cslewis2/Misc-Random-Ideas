
#Starting amount, used amount, defective, added,type of ball,remaining amount
#Table would be nice
#TRY USING LIBRARY AS DATA REPO, FIGURE OUT HOW TO RETRIEVE
#INITIAL BALL STOCK=88

# stock_seed= int (input('initial ball_stock? ' ))
# balls_sold= int  (input('number of balls sold? '))
# stocksum= stock_seed-balls_sold
# print (stocksum)
#balls_used=stock_seed-balls_sold
# USE CONSTANTS??
# PRINCE COUNT=
# WILSON COUNT=
# DUNLOP COUNT=
balls=['Prince','Wilson','Dunlop']

def init_balls():
    '''stock initializer'''
     all_ball_stock=[]
    Prince_stock=input(int('Enter Dunlop,Prince,Wilson quantities...'))
    Wilson_stock=input(int('Enter Dunlop,Prince,Wilson quantities...'))
    Dunlop_stock=input(int('Enter Dunlop
                           quantities...'))
    return [all_ball_stock]


# def Prince():
#     stock_seed= int (input('initial ball_stock? ' ))
#     balls_sold= int  (input('number of balls sold? ')) 
#     stocksum= stock_seed-balls_sold
#     print (stocksum,'prince class')
#     return stocksum

# class calcu:
#     stock_seed= int(input('initial ball stock? ' ))
#     balls_sold= int(input('number of balls sold? '))
#     stocksum= stock_seed-balls_sold
#     print(stocksum,'calcu classer')

# Prince()
# calcu()

# if __name__==main:
#     main()

init_balls()
