from data import data
import random

f = None
count = 0
while(f != 1):
    A = random.choice(data)
    B = random.choice(data)
    if(B == A):
        B = random.choice(data)


    print("Compare A:")
    print(A["name"],",","a",A["description"],",","from",A["country"])
    print("\nVS\n")
    print("Compare B:")
    print(B["name"],",","a",B["description"],",","from",B["country"])

    check = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n")
    if(check == "a"):
        if(A["follower_count"] > B["follower_count"]):
            count = count + 1
        else:
            f = 1

    if(check == "b"):
        if(A["follower_count"] < B["follower_count"]):
            count = count + 1
        else:
            f = 1
    if(f == 1):
        print("YOU LOST. THE END!")
        print(f"THE FINAL SCORE WAS : {count}")
    else:
        print("\n" * 50)
        print(f"You are right! Current score: {count}")



