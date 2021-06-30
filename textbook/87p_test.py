# our_pots={"박재연":2, "맹수연":3}
# for name in our_pots:
#     print(name)
#     print("{}의 집에는 {}개의 냄비가 있다.".format(name, our_pots[name]))
#     if our_pots[name]>=3:
#         print(name)
#         break
#
# for i in range(2,10):
#     for j in range(1, 10):
#         print("{} X {} = {}".format(i,j,i*j))
# i=2
# while(i<10):
#     j=1
#     while(j<10):
#         print("{} X {} = {}".format(i,j,i*j))
#         j=j+1
#     i=i+1
table = [["월", "화","수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col)+" ")
    print()
