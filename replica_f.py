import os
class Replica:
    def __init__(self):
        self.replica_path = input("Insert replica folder path: ")

    def check_path(self):
         if os.path.exists(self.replica_path):
            return True

    def delete_files(self):
        if os.listdir(self.replica_path) != []:
                        for rep_files in os.listdir(self.replica_path):
                            os.remove(self.replica_path + rep_files)

    def write_files(self, dict = {}):
        for file_name, content in dict.items():
                x = open(self.replica_path + file_name, 'w')
                x.write(content)
                x.close()

