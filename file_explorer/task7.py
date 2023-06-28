import pickle

def print_csv_as_pickle(input_file):
    with open(input_file, 'r') as file:
        reader = [line.rstrip() for line in file]
        p = pickle.dumps(reader);           
        print(p)    
            
csv_file = "users_processed2FromPickle.csv"
print_csv_as_pickle(csv_file)
