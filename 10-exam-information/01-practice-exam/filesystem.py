from abc import ABC, abstractmethod
import re


class StorageDevice:
    def __init__(self, block_count, block_size):
        self.__available_blocks = set(range(block_count))
        self.__used_blocks = set()
        self.__block_size = block_size

    @property
    def available_block_count(self):
        return len(self.__available_blocks)

    @property
    def used_block_count(self):
        return len(self.__used_blocks)

    @property
    def total_block_count(self):
        return len(self.__available_blocks)+len(self.__used_blocks)

    @property
    def block_size(self):
        return self.__block_size

    def allocate(self, block_count):
        if self.available_block_count < block_count:
            raise RuntimeError("Not enough blocks availble")
        all_bl = list(self.__available_blocks)[:block_count]
        self.__available_blocks -= set(all_bl)
        self.__used_blocks.update(all_bl)
        return all_bl

    def free(self, blocks):
        for b in blocks:
            if b not in self.__used_blocks:
                raise RuntimeError(f"block {b} is not allocated")
        blocks = set(blocks)
        self.__available_blocks.update(blocks)
        self.__used_blocks -= blocks


class Entity(ABC):
    def __init__(self, storage, name):
        if not self.is_valid_name(name):
            raise RuntimeError("Invalid Name")
        self.__storage = storage
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not self.is_valid_name(new_name):
            raise RuntimeError("Invalid Name")
        self.__name = new_name

    @property
    def storage(self):
        return self.__storage

    @staticmethod
    def is_valid_name(name):
        if not re.fullmatch(r"(\.|[a-zA-Z0-9]){1,16}", name):
            return False
        else:
            return True

    @property
    @abstractmethod
    def size_in_blocks(self):
        pass

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.storage.block_size

    @abstractmethod
    def clear(self):
        pass


class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__allocated_blocks = []

    def grow(self, block_count):
        allocated = self.storage.allocate(block_count)
        self.__allocated_blocks.extend(allocated)

    @property
    def size_in_blocks(self):
        return len(self.__allocated_blocks)

    def clear(self):
        if self.__allocated_blocks:
            self.storage.free(self.__allocated_blocks)
            self.__allocated_blocks.clear()


class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.children = []

    def add(self, entity):
        if not isinstance(entity, (Directory, File)):
            raise RuntimeError("Must be file or directory")
        self.children.append(entity)

    @property
    def size_in_blocks(self):
        total = sum([i.size_in_blocks for i in self.children])
        return total

    def clear(self):
        for child in self.children:
            child.clear()
        self.children = []


# my_ssd = StorageDevice(block_count=1000, block_size=4096)
# directory = Directory(my_ssd, 'myfolder')
#
# Initially, a directory takes no room
# assert directory.size_in_blocks == 0
#
# We add a file
# file1 = File(my_ssd, 'file1')
# file1.grow(5)
# directory.add(file1)
#
# The directory's size is the sum of all of its children's sizes
# assert directory.size_in_blocks == 5
#
# We add a second file
# file2 = File(my_ssd, 'file2')
# file2.grow(10)
# directory.add(file2)
# assert directory.size_in_blocks == 15
#
# We create a subdirectory and add a file to it
# subdir = Directory(my_ssd, 'subdir')
# directory.add(subdir)
# file3 = File(my_ssd, 'file3')
# file3.grow(20)
# subdir.add(file3)
#
# The directory's size has grown
# assert directory.size_in_blocks == 35
#
# All files are cleared recursively
# directory.clear()
# assert directory.size_in_blocks == 0
# assert file1.size_in_blocks == 0
# assert file2.size_in_blocks == 0
# assert file3.size_in_blocks == 0
#
# print("All tests passed!")
#
