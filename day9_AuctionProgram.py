from utils import auction_arts as aa

print(aa.logo)
print("Welcome to the secret auction program.")

bidders = {} 
bidding_finish = False

def find_highest_bidding(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finish:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'.")
    if others == "yes":
        pass
    elif others == "no":
        bidding_finish = True
    else: break
    
find_highest_bidding(bidders)


    