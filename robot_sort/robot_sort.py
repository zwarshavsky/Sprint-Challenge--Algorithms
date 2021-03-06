class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def move_all_the_way_left(self):
        while self.can_move_left() == True:
            self.move_left()
            print(self._position)


    def sort(self):
        """
        Sort the robot's list.
        """
        # for i in range(len(self._list)):
        #     print(i)
        # tested bubble sort below, it worked. obviously, this does not fulfill the requirements.  
        # swapped = True
        # while swapped == True:
        #     swapped = False 
        #     for index in range(len(self._list)-1):
        #         if l[index] > l[index+1]:
        #             l[index],l[index+1] = l[index+1],l[index] 
        #             swapped = True

        # return self._list 

        # replicating the bubble sort using built-in methods in the class
        # first step is to pick up the first item in list

        self.set_light_on()
        while self.light_is_on() == True:
            self.set_light_off()
            while self.can_move_right() == True:
                self.swap_item()
                self.move_right()
                # print(self.compare_item())
                if self.compare_item() is None:
                    print("held item is None")
                    self.swap_item()
                    self.move_right()
                    print(self._position)
                elif self.compare_item() == 1:
                    print("held item is larger than item in front")
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    print("after position:",self._position)
                    self.set_light_on()
                    if self.can_move_right() == False:
                        self.move_all_the_way_left()
                elif self.compare_item() == -1:
                    print("held item is smaller than item in front",self._position)
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    print("after position:",self._position)
                    


        #selection sort code
        # def selection_sort(l=l):
        #     # loop through n-1 elements
        #     for i in range(0, len(l) - 1):
        #         cur_index = i
        #         smallest_index = cur_index
        #         for j in range(cur_index, len(l)):
        #             if l[smallest_index] > l[j]:
        #                 l[smallest_index],l[j] = l[j],l[smallest_index]
        #     return l

        # self.swap_item()
            # for i in range(0, len(robot._list) - 1):
            #     for j in range(self._position,len(robot._list)):
        # while self.can_move_right() == True:
        #     self.swap_item()
        #     self.move_right()
        #     # print(self.compare_item())
        #     if self.compare_item() is None:
        #         print("held item is None")
        #         self.swap_item()
        #         self.move_right()
        #         print(self._position)
        #     elif self.compare_item() == 1:
        #         print("held item is larger than item in front")
        #         self.swap_item()
        #         self.move_left()
        #         self.swap_item()
        #         self.move_right()
        #         print("after position:",self._position)
        #     elif self.compare_item() == -1:
        #         print("held item is smaller than item in front",self._position)
        #         self.move_left()
        #         self.swap_item()
        #         self.move_right()
        #         print("after position:",self._position)


            


            




if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    l = [1,3,2,7,9,4,58,29,18,99]

    robot = SortingRobot(l)
    print(robot.sort())
    print(robot._list)