from collections import Counter
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def draw_graph(search_result):
  date_ranges = ['Jan 1-15', 'Jan 16-31', 'Feb 1-15', 'Feb 16-29', 'Mar 1-15', 'Mar 16-31', 'Apr 1-15']
  counts = [0] * len(date_ranges)

  for doc in search_result:
      date = int(documents[doc]['date'][8:10])
      month = int(documents[doc]['date'][5:7])

      if month == 1:
          if 1 <= date <= 15:
              counts[0] += 1
          elif 16 <= date <= 31:
              counts[1] += 1
      elif month == 2:
          if 1 <= date <= 15:
              counts[2] += 1
          elif 16 <= date <= 29:
              counts[3] += 1
      elif month == 3:
          if 1 <= date <= 15:
              counts[4] += 1
          elif 16 <= date <= 31:
              counts[5] += 1
      elif month == 4:
          if 1 <= date <= 15:
              counts[6] += 1


  plt.bar(date_ranges, counts, color='skyblue')
  plt.title('Article Distribution from January to April')
  plt.xlabel('Date Range')
  plt.ylabel('Number of Articles')
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show()