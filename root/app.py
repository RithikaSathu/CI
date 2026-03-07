from model import train_model, predict

def main():

    model = train_model()

    value = 6
    prediction = predict(model,value)

    print("Prediction for",value,"is",prediction)


if __name__ == "__main__":
    main()