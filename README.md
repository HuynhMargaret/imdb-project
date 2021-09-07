# imdb-project
A simple project to identify good movies for dinners

Data sources including:
  - imdb datasets: downloaded from https://datasets.imdbws.com/ 
  - Further data for movies, cast & crews (unavailable in imdb datasets above): collected by Python scripts - get_additional_movie_info.py for movies & get_additional_castcrew_info.py for cast and crew, using IMDbPY library

Some data analysis exercises were done, using Python (data_analysis_python.py) & SQL (data_analysis_sql.txt), including:
  - Calculate Bayesian average rating (source: https://www.codementor.io/@arpitbhayani/solving-an-age-old-problem-using-bayesian-average-15fy4ww08p)
  - Find all years that have a movie that received a rating of 9 and above
  - Find the difference between the average rating of movies released before 1980 and the average rating of movies released after 1980 (Answer: Older movies are rated better)
  - More to come...

Data visualization dashboard is created with Microsoft Power BI (imdb-top-movies-dashboard.pbix)

Future planing for project:
  - Futher data analysis in Python with matplotlib, seaborn, etc.
  - Explore data modelling of movie information (plot, genres, cast, etc.) to recommend good movies, with ambition to learn and apply Natural Language Processing & Machine Learning frameworks
