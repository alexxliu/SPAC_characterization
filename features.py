import pickle
import spac
import spac.visualization
import matplotlib.pyplot as plt
import time

def get_input():
    return {
        "h1_feat": "",   # Replace with actual feature
        
    }
input_values = get_input()

# Loading the dataset
file_path = "/anvil/projects/tdm/corporate/fnl-spatial/Spring_2025/Data/resampled_data_10000.pickle" #Update with every dataset
with open(file_path, 'rb') as file:
    adata = pickle.load(file)

#Start time in the features visualization
begin_time = time.time()

#Loads the features visualization
fig1 = spac.visualization.histogram(adata, feature=input_values["h1_feat"])
#End time
end_time = time.time()
run_time = end_time - begin_time
print("Features run time: {:.4f} seconds".format(run_time))


plt.savefig('test_features.png')




