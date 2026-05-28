with open("text.txt","w") as f:
    f.write("Hellow World")
with open("text.txt","r") as f:
    data=f.read()
                
print(data)