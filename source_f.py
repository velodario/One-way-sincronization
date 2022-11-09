import os
class Source:
      def __init__(self):
        self.source_path = input("Insert source folder path: ")


      def check_path(self):
         if os.path.exists(self.source_path):
            return True

      def read_files(self):
         dict = {}
         for f in os.listdir(self.source_path):
            with open(self.source_path + f, 'r') as x:
                dict[f] = x.read()
                x.close()
         return dict

