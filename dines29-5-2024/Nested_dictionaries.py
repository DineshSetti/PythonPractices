data={
   "ram":{"name":"dinesh","roll_no":22,"branch":"cse","phn_no":1234},
    "shyam":{"name":"mahesh","roll_no":25,"branch":"cse"}
}
print(data["ram"]["roll_no"])
data["shyam"]["phn_no"]=9876
print(data["shyam"]["phn_no"])
print(data["shyam"])