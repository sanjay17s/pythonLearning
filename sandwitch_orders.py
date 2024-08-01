sandwich_orders=["butter sandwitch","cheese sandwitch","paneer sandwitch",'pastrami','pastrami','pastrami']

while sandwich_orders:
    sandwitch = sandwich_orders.pop()
    print(f"i made you a {sandwitch} and movinf it to finished sandwitch")
    finished_sandwiches.append(sandwitch)
print("all sandwitches are made")   
print(f"initial order: {sandwich_orders}") 
print(f"final: {finished_sandwiches}")