#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// Define a structure for movie ratings
struct Rating {
    int user_id;
    int movie_id;
    double rating;
};

// Function to get recommendations for a user
vector<int> get_recommendations(int user_id, const unordered_map<int, vector<Rating>>& ratings, int top_n = 10) {
    vector<int> recommendations;
    unordered_map<int, double> scores;
    
    // Loop through all movies
    for (const auto& entry : ratings) {
        int movie_id = entry.first;
        const vector<Rating>& movie_ratings = entry.second;
        
        // Calculate score based on collaborative filtering (simple averaging here)
        double score_sum = 0.0;
        int count = 0;
        for (const Rating& rating : movie_ratings) {
            score_sum += rating.rating;
            count++;
        }
        
        if (count > 0) {
            double average_score = score_sum / count;
            scores[movie_id] = average_score;
        }
    }
    
    // Sort movies by score (descending) and get top-N recommendations
    vector<pair<int, double>> sorted_scores(scores.begin(), scores.end());
    sort(sorted_scores.begin(), sorted_scores.end(), [](const pair<int, double>& a, const pair<int, double>& b) {
        return a.second > b.second;
    });
    
    for (size_t i = 0; i < min(top_n, static_cast<int>(sorted_scores.size())); ++i) {
        recommendations.push_back(sorted_scores[i].first);
    }
    
    return recommendations;
}

int main() {
    // Sample movie ratings data (user_id, movie_id, rating)
    unordered_map<int, vector<Rating>> ratings = {
        {1, {{1, 101, 4.5}, {1, 102, 3.0}, {1, 103, 2.5}}},
        {2, {{2, 101, 5.0}, {2, 102, 4.0}, {2, 103, 3.5}}},
        {3, {{3, 101, 3.5}, {3, 102, 2.0}, {3, 103, 4.5}}},
        // Add more user ratings as needed
    };
    
    // Get recommendations for user ID 1
    int user_id = 1;
    vector<int> recommended_movies = get_recommendations(user_id, ratings);
    
    // Display recommendations
    cout << "Top recommended movies for user " << user_id << ":" << endl;
    for (int movie_id : recommended_movies) {
        cout << "- Movie ID: " << movie_id << endl;
    }
    
    return 0;
}
