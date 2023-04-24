import matplotlib.pyplot as plt

# Function to read data from a file and return a list of columns
def read_data_file(file_path):
    data = [[] for i in range(4)]
    with open(file_path, 'r') as f:
        for line in f:
            values = line.strip().split(',')
            for i in range(4):
                data[i].append(float(values[i]))
    return data

# Read data from the two files
file1_data = read_data_file('withAlgoDensity.csv')
file2_data = read_data_file('withoutAlgoDensity.csv')

# Generate a graph for each column and save as PNG file
for i in range(4):
    plt.plot(file1_data[i], label='File 1')
    plt.plot(file2_data[i], label='File 2')
    plt.legend()
    plt.xlabel('Data Points')
    plt.ylabel('Column {}'.format(chr(ord('A') + i)))
    plt.savefig('column_{}.png'.format(i+1))
    plt.clf()  # clear the plot for the next column