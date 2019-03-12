from PlanesAndTrains import *

workload = UMD()

# input from keyboard and validating every input condition to avoid errors from human inputs
# first line
input_first_line = input("Enter 4 integers separated by commas: t, p, nt, np. 0<=t<100, 0<=p<10, 0<=nt, 0<=np \n")
first_input = input_first_line.split()
number_of_trains = int(first_input[0])
number_of_planes = int(first_input[1])
total_num_of_train_items = int(first_input[2])
total_num_of_plane_items = int(first_input[3])
if first_input.__len__() != 4:
    raise Exception("Exactly 4 integers should be entered. User has given "+str(first_input.__len__())+" integers")
if number_of_trains < 0 or number_of_trains > 100:
    raise Exception("t value entered is not correct")
if number_of_planes < 0 or number_of_planes > 10:
    raise Exception("p value entered is not correct")
if total_num_of_train_items < 0:
    raise Exception("nt value entered is not correct")
if total_num_of_plane_items < 0:
    raise Exception("np value entered is not correct")

# second line
input_second_line = input("Enter items to be loaded to " + str(number_of_trains) + " trains: \n")
items_to_each_train = input_second_line.split()
if items_to_each_train.__len__() != number_of_trains:
    raise Exception(str(number_of_trains)+" integers should be entered.")
sum_of_num_of_train_items = 0
for i in range(items_to_each_train.__len__()):
    sum_of_num_of_train_items += int(items_to_each_train[i])
if sum_of_num_of_train_items != total_num_of_train_items:
    raise Exception("Item numbers given in second line should sum up to " + str(total_num_of_train_items))

# third line
input_third_line = input("Enter items to be loaded to " + str(number_of_planes) + " planes: \n")
items_to_each_plane = input_third_line.split()
if items_to_each_plane.__len__() != number_of_planes:
    raise Exception(str(number_of_planes) + " integers should be entered.")
sum_of_num_of_planes_items = 0
for j in range(items_to_each_plane.__len__()):
    sum_of_num_of_planes_items += int(items_to_each_plane[j])
if sum_of_num_of_planes_items != total_num_of_plane_items:
    raise Exception("Item numbers given in third line should sum up to " + str(total_num_of_plane_items))

# fourth line
input_fourth_line = input("Enter destinations of " + str(sum_of_num_of_train_items) +
                                " items to be loaded to " + str(number_of_trains) + " trains: \n")
destination_of_train_items = input_fourth_line.split()
if destination_of_train_items.__len__() != sum_of_num_of_train_items:
    raise Exception("Exactly "+str(sum_of_num_of_train_items)+" integers should be entered.")
sum_of_num_of_train_destination_numbers = 0
for m in range(destination_of_train_items.__len__()):
    sum_of_num_of_train_destination_numbers += int(destination_of_train_items[m])
sum_to_be = 0   # validating if the destinations are correct (validating between 2nd and 4th input lines)
for n in range(items_to_each_train.__len__()):
    sum_to_be += (int(items_to_each_train[n]) * (n + 1))
if sum_of_num_of_train_destination_numbers != sum_to_be:
    raise Exception("Please check the train items destinations. Values do not match with the second line")

# fifth line
input_fifth_line = input("Enter destination of " + str(sum_of_num_of_planes_items) +
                            " items to be loaded to " + str(number_of_planes) + " planes: \n")
destination_of_plane_items = input_fifth_line.split()
if destination_of_plane_items.__len__() != sum_of_num_of_planes_items:
    raise Exception("Exactly " + str(sum_of_num_of_planes_items) + " integers should be entered.")
sum_of_num_of_plane_destination_numbers = 0
for o in range(destination_of_plane_items.__len__()):
    sum_of_num_of_plane_destination_numbers += int(destination_of_plane_items[o])
sum_to_be_ = 0  # validating if the destinations are correct (validating between 3rd and 5th input lines)
for p in range(items_to_each_plane.__len__()):
    sum_to_be_ += (int(items_to_each_plane[p]) * (p + 1))
if sum_of_num_of_plane_destination_numbers != sum_to_be_:
    raise Exception("Please check the plane items destinations. Values do not match with the third line")

# Pass inputs and get time for loading items to trains and planes
output_tuple = workload.calculate_time(number_of_trains, number_of_planes, destination_of_train_items, destination_of_plane_items)

# print_output
train_times, plane_times = output_tuple
train_times = str(train_times).replace("[", "").replace("]", "").replace(",", "")
plane_times = str(plane_times).replace("[", "").replace("]", "").replace(",", "")
print(train_times)
print(plane_times)
