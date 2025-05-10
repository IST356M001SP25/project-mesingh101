# Reflection

Student Name:  name
Student Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

Working on this NBA stats comparison app helped me grow in multiple areas—especially API integration, error handling, and building interactive user interfaces with Streamlit. The project required pulling season average stats from the BallDon'tLie API, transforming that data into clean DataFrames, and visualizing it with Plotly. Setting up that full pipeline taught me how to manage real-world data sources and build a meaningful user experience around them.

One of the biggest challenges I faced was dealing with limited API access. Initially, I kept running into errors when trying to retrieve season average data—specifically getting 401 Unauthorized or incomplete responses. After some debugging and reviewing the API documentation, I realized that some endpoints, like season_averages, weren’t accessible on the free tier. To move forward, I purchased an account upgrade, which unlocked the functionality I needed to continue building and testing my app. This taught me how third-party APIs are tiered and how important it is to understand access limitations early on.

Even after upgrading, there were still some inconsistencies in available data for certain players or seasons. That required building in UI messages to let users know when results couldn't be retrieved and handling empty responses gracefully.

Overall, this project strengthened my confidence with APIs, especially when it comes to authentication, pagination, and parsing JSON data. I also got better at debugging and reading error messages. If I were to keep improving the app, I’d add caching for player data, allow users to export comparisons, and maybe even incorporate advanced stats for deeper analysis.