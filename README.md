The purpose of the project was to look at posts from a subreddit, get information about the words used and see what sort of categories were involved in the posts. I chose the subreddit r/LifeProTps.

I took a collection of thousands of posts from the subreddit and selected around 1,000 to use. I chose the posts that had the most upvotes. I then split each post into the separate words and kept the words that were used at least 6 times, which ended up being around 600 words. 

To do this, I used Spacy to turn all the posts into a pipeline of words. I then tokenized the words while removing a few common ones such as "a","be","in", etc, and joined them as one sentence for each post. This led to a dataframe of each post, a list of the words from the original spacy document for each post, and the cleaned list of words as one long string for each post. I then transformed just the cleaned list into a list of strings. 

Then using CountVectorizer, I obtained a count of each word in each string in the list and displayed it as an array. This array came with some weird "words" such as "199x", words that had äú in front of them, and numbers. So, I dropped all columns of the array which contained these unwanted words. I then got the sum for each word and transformed it into a dataframe of the word and the sum which was exported as a CSV. 

This CSV was put into the folder for the streamlit project. I chose to do 3 main pages for the app, excluding the Welcome page.

The first page showed all the words and their sum. 

The second page, allows the user to select any number of specific words. This will show each words and their sum, and a bargraph of the selected words. 

The third page allows the user to select a category which contains preselected words. These categories include 'Romance', 'Work', 'Technology', 'Family', 'Frequency', 'Health', 'School', 'Relationships', 'Money', 'Entertainment', 'Events', and 'Pets'. I created a function where the input is a category, with an empty dataframe. For each category, there is a set of words and the code looks to see which of those words are in the original dataframe of words and sums. If the word exists, it is added to the empty dataframe which is then returned. Those words are then shown in a bargraph with the sum of each word.
