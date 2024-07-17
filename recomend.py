import numpy as np

# Sample user data with movie ratings (1-5)
users = {
    "Alice": {"Action": 4, "Comedy": 3, "Thriller": 5},
    "Bob": {"Action": 5, "Comedy": 1, "Drama": 4},
    "Charlie": {"Comedy": 4, "Romance": 5, "Thriller": 2},
    "David": {"Action": 1, "Drama": 3, "Romance": 4}
}

# Function to calculate cosine similarity between users
def cosine_similarity(user1, user2):
  dot_product = np.dot(list(user1.values()), list(user2.values()))  # Replace with numpy.dot for actual implementation
  magnitude1 = np.linalg.norm(list(user1.values()))  # Replace with numpy.linalg.norm for actual implementation
  magnitude2 = np.linalg.norm(list(user2.values()))  # Replace with numpy.linalg.norm for actual implementation
  return dot_product / (magnitude1 * magnitude2) if magnitude1 > 0 and magnitude2 > 0 else 0

# Function to recommend movies for a user
def recommend_movies(user, k=3):
  # Calculate similarity scores with other users
  similarities = {}
  for other_user, ratings in users.items():
    if other_user != user:
      similarities[other_user] = cosine_similarity(users[user], ratings)

  # Find k most similar users
  nearest_neighbors = sorted(similarities.items(), key=lambda item: item[1], reverse=True)[:k]

  # Recommend movies based on weighted ratings from neighbors
  recommendations = {}
  for neighbor, similarity in nearest_neighbors:
    for movie, rating in users[neighbor].items():
      if movie not in users[user]:
        if movie not in recommendations:
          recommendations[movie] = 0
        recommendations[movie] += similarity * rating

  # Recommend top N movies with highest weighted ratings
  return sorted(recommendations.items(), key=lambda item: item[1], reverse=True)[:k]

# Function to display movie information (placeholder for actual data retrieval)
def get_movie_info(movie_title):
  # Simulate movie information retrieval (replace with actual implementation)
  info = f"Movie not found: {movie_title}"
  if movie_title == "The Matrix":
    info = f"{movie_title} (1999) - Sci-fi action film directed by the Wachowski brothers."
  return info

# Example usage: Recommend movies for Alice
alice_recommendations = recommend_movies("Alice")

# Print recommendations with movie information
print("Recommended movies for Alice:")
for movie, weighted_rating in alice_recommendations:
  movie_info = get_movie_info(movie)
  print(f"- {movie} (weighted rating: {weighted_rating:.2f}) - {movie_info}")
