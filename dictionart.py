info = {
    "name" : "jatin",
    "placement" : 11.5,
    "designation" : "JavaDeveloper",
    "cgpa" : {
        "first" : 6.6,
        "seccond" : 7.2,
        "third" : 7.8,
        "forth" : 8.2
    }
}
print (info["name"])
print(info["cgpa"]["forth"])
print(info.update({"college":"GL Bajaj"}))
print(info)
coll = info.pop("college")
print(coll)
print(info)