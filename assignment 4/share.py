amount=int(input("total bill amount="))
gst=0.05*amount
service = 0.10*amount
friends=int(input("Number of friends ="))
bill= amount+gst+service
share= bill/friends
print("final bill=", bill)
print("each person pays= ",share)