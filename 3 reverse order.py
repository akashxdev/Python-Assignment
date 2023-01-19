f1 = open("output1.txt", "w")


with open("input1.txt", "r") as myfile:
	data = myfile.read()

data_1 = data[::-1]

f1.write(data_1)

print("File generated sucessfully")

f1.close()
