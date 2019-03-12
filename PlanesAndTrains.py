from StackQueue import MyStack, CircularQueue


class UMD:
    MAX_TRAIN_MATERIAL_STACK = 5

    def __init__(self):
        self.train_items_stack = MyStack()
        self.plane_items_queue = CircularQueue()
        self.time_train_finished_loading = 0
        self.time_plane_finished_loading = 0

    def load_items_to_train(self, list_of_train_loading_time):
        for loop in range(0, 5):
            pop_ = self.train_items_stack.pop()
            self.time_train_finished_loading += int(pop_)   # loading time
            list_of_train_loading_time[(int(pop_) - 1)] = self.time_train_finished_loading
            self.time_train_finished_loading += int(pop_)  # worker coming back
            if self.train_items_stack.__len__() == 0:
                break

    def load_items_to_plane(self, list_of_plane_loading_time):
        dequeue_ = self.plane_items_queue.dequeue()
        self.time_plane_finished_loading += (int(dequeue_) * 5)   # loading time
        list_of_plane_loading_time[(int(dequeue_) - 1)] = self.time_plane_finished_loading
        self.time_plane_finished_loading += (int(dequeue_) * 5)     # worker coming back

    def calculate_time(self, number_of_trains, number_of_planes,
                       destination_of_train_items, destination_of_plane_items):
        # creating lists to store times of each train and plane
        list_of_train_loading_time = [0] * number_of_trains
        list_of_plane_loading_time = [0] * number_of_planes

        # trains - stack
        number_of_train_items = destination_of_train_items.__len__()
        index = 0
        while self.train_items_stack.__len__() <= UMD.MAX_TRAIN_MATERIAL_STACK:
            self.train_items_stack.push(destination_of_train_items[index])
            index += 1
            number_of_train_items -= 1
            if self.train_items_stack.__len__() == UMD.MAX_TRAIN_MATERIAL_STACK or number_of_train_items == 0:
                UMD.load_items_to_train(self, list_of_train_loading_time)
            if number_of_train_items == 0:  # to break the loop
                break

        # planes - queue
        for loop in range(0, destination_of_plane_items.__len__()):
            self.plane_items_queue.enqueue(destination_of_plane_items[loop])
        while self.plane_items_queue.__len__() != 0:
            UMD.load_items_to_plane(self, list_of_plane_loading_time)

        return list_of_train_loading_time, list_of_plane_loading_time
