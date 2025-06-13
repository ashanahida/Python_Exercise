import os
print("===========Welcome to 10BX Slient Auction Game============")

def find_winner(bidder_details):#{dipu:500 himu:1000 ram:800}
    highest_bid = 0 #1000
    winner=""
    for bidder in bidder_details:#jenny
        bid_price =bidder_details[bidder] #500
        if bid_price>highest_bid:
            highest_bid=bid_price
            winner = bidder
    print(f"The winner is {winner} with {highest_bid} bid price")


bidders_info ={}

bidding_end = False
while not bidding_end:

    name = input("Enter bider name here: \n")
    bid_money = int(input("Bid the money here: \n"))
    bidders_info[name] = bid_money
    confirm = input("Are there more bidders? 'yes' or 'no' : \n").lower()
    if confirm == 'no':
        bidding_end = True
        find_winner(bidders_info)
    elif confirm == 'yes':
        os.system('cls') #clear screen