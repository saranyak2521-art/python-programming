library = [{"title":"Book A","author":"Author A","available":True},
           {"title":"Book B","author":"Author B","available":True},
           {"title":"Book C","author":"Author C","available":True}]
borrowed = {}

def display(): print("\nAvailable:", [b["title"] for b in library if b["available"]])

def borrow(user,title):
    for b in library:
        if b["title"]==title:
            if b["available"]:
                b["available"]=False
                borrowed[user]=borrowed.get(user,[])+[title]
                print(f"{title} borrowed by {user}")
            else: print(f"{title} not available")
            return
    print(f"{title} not found")

def return_book(user,title):
    if user in borrowed and title in borrowed[user]:
        borrowed[user].remove(title)
        for b in library:
            if b["title"]==title: b["available"]=True
        print(f"{title} returned by {user}")
    else: print(f"{user} did not borrow {title}")

# Example
display()
borrow("Alice","Book A")
borrow("Bob","Book A")
display()
return_book("Alice","Book A")
display()
