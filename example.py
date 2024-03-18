import pickle

with open("house_predictor.pickle", "rb") as file:
    loaded_model = pickle.load(file)
    