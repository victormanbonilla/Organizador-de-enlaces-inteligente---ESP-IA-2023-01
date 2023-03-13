import pickle
import sklearn


# Abre el archivo en modo binario para cargar el modelo
with open('./models/prod_feature_extractor.pkl', 'rb') as archivo:
    extractor = pickle.load(archivo)

with open('./models/prod_model_naive.pkl', 'rb') as archivo:
    model_naive = pickle.load(archivo)
    
categories = {
    0: "Travel",
    1: "Social Networking and Messaging",
    2: "News",
    3: "Streaming Services",
    4: "Sports",
    5: "Photography",
    6: "Law and Government",
    7: "Health and Fitness",
    8: "Games",
    9: "E-Commerce",
    10: "Forums",
    11: "Food",
    12: "Education",
    13: "Computers and Technology",
    14: "Business/Corporate",
    15: "Adult"
}