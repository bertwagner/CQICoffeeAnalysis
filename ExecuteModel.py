import pandas as pd
import numpy as np
import joblib

def null_altitude_outliers(X):
    X[X < 200] = None
    X[X > 5000] = None
    return X

model = joblib.load("coffee_model.pkl") 

data = pd.DataFrame(index=np.arange(0, 1),columns = ['Species', 'Owner', 'Country.of.Origin', 'Farm.Name', 'Lot.Number',
       'Mill', 'ICO.Number', 'Company', 'Altitude', 'Region', 'Producer',
       'Number.of.Bags', 'Bag.Weight', 'In.Country.Partner', 'Harvest.Year',
       'Grading.Date', 'Owner.1', 'Variety', 'Processing.Method', 'Aroma',
       'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity',
       'Clean.Cup', 'Sweetness', 'Cupper.Points', 'Moisture',
       'Category.One.Defects', 'Quakers', 'Color', 'Category.Two.Defects',
       'Expiration', 'Certification.Body', 'Certification.Address',
       'Certification.Contact', 'unit_of_measurement', 'altitude_low_meters',
       'altitude_high_meters', 'altitude_mean_meters'])

data["Country.of.Origin"] = "Kenya"
data["Variety"] = "Bourbon"
data["Processing.Method"] = "Natural / Dry"
data["altitude_mean_meters"] = 2000

result = model.predict(data)
print(result)