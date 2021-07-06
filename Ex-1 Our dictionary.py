#Our Dictionary

Dict={"laptop":"use to simplyfy things",
      "moblile":"use to communicate with people easily in any area of the word",
      "email":"to send text, doc, pictures and many more",
      "python":"easy programmimg language to develop software",
      "tv":"to see the news and get entertained by it"}
use=input("the use of ")
print(Dict[use])
print(Dict)
print(Dict.keys())
print(Dict.get("laptop"))
x=Dict.keys()
print(x)
y=Dict.values()
print(y)
print("laptop" in Dict)
if "laptop" in Dict:
    print("you are great")
