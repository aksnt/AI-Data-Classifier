import math
import csv
import sys

#Function that simply calculates Euclidean distance between two points and returns it
def get_ed(x1,x2, attributes, ed):
    for point in range(attributes-1):
        ed += math.pow(x1[point] - x2[point],2)
    return math.sqrt(ed)

#Function that stores training filename in a 2D list/array
def get_training_file(training_filename):
    training_file = []
    with open(training_filename) as tf:
        tr = csv.reader(tf, delimiter = ",")
        attributes = len(next(tr)) #Used to retrieve number of attributes
        
        #Nested for loops to create a 2D List and store each row of the training file
        for row in tr:
            tdr = []
            for i in range(attributes-1):
                #convert string to float for use in later calculations
                tdr.append(float(row[i])) 
            #append the class variable at end
            tdr.append(row[attributes-1]) 
            training_file.append(tdr)
    tf.close()
    return training_file

#Function that stores testing filename in a 2D list/array
def get_testing_file(testing_filename):
    testing_file = []
    with open(testing_filename) as tf:
        tr = csv.reader(tf, delimiter = ",")
        for line in tr:
            tr_row = []
            for data in line:
                tr_row.append(float(data))
            testing_file.append(tr_row)
    tf.close()
    return testing_file
    

def classify_nn(training_filename, testing_filename, k):  
    
    #Initialise files using their respective functions
    training_file = get_training_file(training_filename)
    testing_file = get_testing_file(testing_filename)
    k = int(k) #convert k to an int type 
    
    #length of the first row in training file = num of attributes
    attributes = len(training_file[0]) 
    
    #final results will be stored here
    results = [] 
    
    #For each x1 in the testing file, and x2 in training file, calculate their Euclidean distance
    for x1 in testing_file:
        #Store the Euclidean distance in this array
        features = []
        for x2 in training_file:
            ed1 = 0
            ed1 += get_ed(x1, x2, attributes, ed1)
            features.append([ed1, x2[-1]])
        #Sort them for use below
        features.sort(key=lambda x: x[0])
        
        #Initialise yes/no variables to count each variable
        yes = no = 0
        features_label = []
        
        #For every neighbour found in range(k), we append their label to our array
        for neighbour in range(k):
            features_label.append(features[neighbour][1])
        for label in features_label:
            if label == "yes":
                yes +=1
            elif label == "no":
                no+=1
        if no > yes:
            results.append('no')
        #In the event of a tie, we prioritise yes
        elif yes >= no:
            results.append('yes')
                
    return print(results)

if __name__ == "__main__":
    training_filename = sys.argv[1]
    testing_filename = sys.argv[2]
    k = sys.argv[3]
    
    classify_nn(training_filename, testing_filename, k)