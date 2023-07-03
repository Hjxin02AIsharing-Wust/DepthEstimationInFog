# filenames='day_train_all/24383'
# line = filenames.split('/')
# folder = line[0]
#
#         # if len(line) == 3:
# frame_index = int(line[1])
# print(frame_index)
def readlines(filename):
    """Read all the lines in a text file and return as a list
    """
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines
filenames=readlines('3.txt')
x=len(filenames)
print(x)
for i in range(x):
    line = filenames[i].split('/')
    folder = line[0]

        # if len(line) == 3:
    frame_index = int(line[1])
    print(frame_index)