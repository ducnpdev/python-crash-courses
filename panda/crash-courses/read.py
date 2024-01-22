import pandas as pd


def handleClient(client=""):
    new = client
    if client == "cif":
        new = "22222222"
        return True, new

    if client == "88888800":
        new = "33333333"
        return True,new

    if client == True:
        new = "44444444"
        return True,new

    return False ,new

print("start read file json")
# Specify the path to your JSON file

json_file_path = "1record.json"

# Read JSON file into a Pandas DataFrame
df = pd.read_json(json_file_path)
print(df)

for index, row in df.iterrows():
    print("index",index)
    print("row",row)
    # Access data in each row
    # item = row['Item']
    clientNoObj = row["CLIENT_NO"]
    print("clientNoObj",clientNoObj)

    # client = ""
    # try:
    #     # print("clientNo", clientNoObj["S"])
    #     client=clientNoObj["S"]
    # except:
    #     # print("except")
    #     # print("clientNo NULL",clientNoObj["NULL"])
    #     client = clientNoObj["NULL"]
    # # else:
    
    # print("else client", client)

    # handleCif = handleClient(client)
    # if handleCif[0] == False:
    #     continue


    # if index == 100:
    #     break    
    # # get clientNO

    # # override 

    # # gen cli


    # print("handle client", handleCif[0],handleCif[1])

# Display the DataFrame
# print(df)


