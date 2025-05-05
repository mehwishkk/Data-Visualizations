import matplotlib.pyplot as plt
x=["python", "c", "c++" ,"Java"]
y=[85,70,60,82]
plt.xlabel("language", fontsize=15)
plt.ylabel("No. of users")
plt.title("Programming Language Popularity")
plt.bar(x,y)
plt.show()
