
# 🎥 Movie Recommender System

Welcome to the **Movie Recommender System** project! This application is designed to suggest the top 5 movies similar to a user-selected movie, providing a seamless and personalized movie discovery experience. It utilizes machine learning algorithms and movie metadata to generate accurate and relevant recommendations.

## 🚀 Features

- **Interactive User Interface**: Built with [Streamlit](https://streamlit.io/), the application offers an intuitive and easy-to-use interface for movie selection and recommendation display.
- **Accurate Recommendations**: Employing a content-based recommendation engine, the system suggests movies based on the similarity of metadata, such as genres, directors, and actors.
- **Dynamic Poster Display**: Retrieves movie posters dynamically using the [TMDb API](https://www.themoviedb.org/documentation/api) to enhance the visual appeal of the recommendations.
- **Real-Time Interaction**: Instant feedback and display of recommendations upon movie selection.

## 🔧 Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/movies-recommender-system.git
   cd movies-recommender-system
   ```

2. **Install required packages**:

   Ensure you have Python 3 installed. Then, use the following command to install the necessary libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your TMDb API key**:

   - Sign up for an account at [The Movie Database (TMDb)](https://www.themoviedb.org/) if you haven’t already.
   - Navigate to your account settings to get your API key.
   - Replace the placeholder API key in the code with your actual API key.

4. **Run the application**:

   ```bash
   streamlit run app.py
   ```

## 📚 Usage

1. Open the application in your browser. You will see a dropdown menu with a list of movies.
2. Select your favorite movie from the dropdown list.
3. Click the "Show Recommendation" button.
4. The application will display the top 5 movies similar to your selected movie, along with their posters and titles.

## 📌 Important Note

Due to recent restrictions on the TMDb API in India, some users might experience issues with poster retrieval. If you are accessing the application from India, you might see a placeholder image instead of the actual movie poster. Despite this limitation, the recommendation engine works flawlessly, providing you with the top movie suggestions based on your choice. We are actively exploring alternative solutions to enhance the visual elements of our application for all users.

## 🛠️ Project Structure

- `app.py`: The main Python script to run the Streamlit application.
- `movie_dict.pkl`: A pickle file containing the movie metadata.
- `similarity.pkl`: A pickle file containing the precomputed similarity matrix.
- `requirements.txt`: A text file listing all the required Python libraries for the project.

## 🌟 Highlights

This project is a great example of how machine learning and data visualization can be used to create an interactive and engaging web application. The Movie Recommender System can be adapted and expanded for different use cases, such as book recommendations, music playlists, or any other domain where personalized content delivery is valuable.



By following this README, users should be able to understand, install, and effectively use your movie recommender system project. It also provides transparency about the current limitations and future plans, making the project attractive to potential contributors and users.
