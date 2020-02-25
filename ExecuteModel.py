import pandas as pd
import numpy as np
import joblib
coffee_model_loaded = joblib.load("coffee_model.pkl")

#data = pd.DataFrame(index=np.arange(1), columns=np.arange(42))

# data["Country.of.Origin"] = "Kenya"
# data["Variety"] = "Bourbon"
# data["Processing.Method"] = "Natural / Dry"
# data["altitude_mean_meters"] = 2000

# result = full_pipeline_with_predictor.predict(data)