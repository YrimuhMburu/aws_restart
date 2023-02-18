userReply = input(" Do you need to ship a package (Enter yes or no)")
if userReply == "yes" :
  print(" we can help you ship the package")
else :
  print("please come back again when you need to ship a package")
userReply = input("Would you like to buy stamps, buy envelopes or  make a copy? (Enter, stamps, envelopes or copy")
if userReply == "stamps":
   print("we have  stamp designs from")
elif userReply == "envelopes":
    print("we have different size of envelopes to choose from")
elif userReply == " copy":
    print("How many copies would you like to make? (Enter a number of copies")
    print(" Here are {} copies .format(copies)")
else:
    print("thank you and come again")