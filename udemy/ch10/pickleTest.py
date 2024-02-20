import pickle

# x = 10
# y = 100
# my_list = [1, 2, 3, 4, 5, 6]

# def save_data():
#     global x, y, my_list
#     data = {"x" : x, "y": y, "my_list" : my_list}

#     with open("my_pickle_file", "wb") as pfile:
#         pickle.dump(data, pfile)

# save_data()

x = None
y = None
my_list = None

def restore_data():
    global x, y, my_list
    with open("my_pickle_file", "rb") as pfile:
        data = pickle.load(pfile)
        x = data["x"]
        y = data["y"]
        my_list = data["my_list"]
        print(x, y, my_list)
restore_data()