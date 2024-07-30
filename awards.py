# the awards that person competing in trialthon will receive, regardless of sport on the fields that day namely swimming,cyling and running.

swim =int(input("enter time taken for swimming in minutes :"))
print("time taken for swimming task:",swim)

cycl =int(input("enter time taken for cycling in minutes :"))
print("time taken for cycling task:", cycl)

run =int(input("enter time taken for running in minutes :"))
print("time taken for running task:",run)

total_time =swim+cycl+run
print("total time taken for triathlon:",total_time)

if (total_time<100):
    print("provincial colors")
elif (total_time>100 and total_time <=105):
    print("provincial half colors")
elif (total_time>105 and total_time <110):
    print("provincial scroll")
else :
    print("no award")