from mrjob.job import MRJob
class Sample_count(MRJob):
   def mapper(self, _, line):
       for word in line.split():
           if word.lower() == "sample":
               yield "sample", 1

   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Sample_count.run()