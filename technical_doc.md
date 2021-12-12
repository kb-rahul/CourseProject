# Technologies:
We use four opensource technology to enable our tool:
* [Twint](https://github.com/twintproject/twint)
* [Sentence Transformer](https://github.com/UKPLab/sentence-transformers)
* [Annoy](https://github.com/spotify/annoy)
* [Streamlit](https://github.com/streamlit/streamlit)

## [Twint](https://github.com/twintproject/twint)
-----------
Twint is an advanced Twitter scraping tool written in Python that allows for scraping Tweets from Twitter profiles without using Twitter's API.

Twint utilizes Twitter's search operators to let you scrape Tweets from specific users, scrape Tweets relating to certain topics, hashtags & trends, or sort out sensitive information from Tweets like e-mail and phone numbers.
Twint also makes special queries to Twitter allowing you to also scrape a Twitter user's followers, Tweets a user has liked, and who they follow without any authentication, API, Selenium, or browser emulation.


## [Sentence Transformer](https://github.com/UKPLab/sentence-transformers)
-------------------
Sentence Transformer framework provides an easy method to compute dense vector representations for sentences, paragraphs, and images. The models are based on transformer networks like BERT / RoBERTa / XLM-RoBERTa etc. and achieve state-of-the-art performance in various task. Text is embedding in vector space such that similar text is close and can efficiently be found using cosine similarity.

## [Annoy](https://github.com/spotify/annoy)
--------------------
Annoy (Approximate Nearest Neighbors) is a C++ library with Python bindings to search for points in space that are close to a given query point. It also creates large read-only file-based data structures that are mmapped into memory so that many processes may share the same data.

Futher, annoy has the ability to use static files as indexes. In particular, this means you can share index across processes. Annoy also decouples creating indexes from loading them, so you can pass around indexes as files and map them into memory quickly. Another nice thing of Annoy is that it tries to minimize memory footprint so the indexes are quite small.

## [Streamlit](https://github.com/streamlit/streamlit) 
Streamlit lets you turn data/model scripts into sharable web apps. 


# Architecture
![Image](https://github.com/kb-rahul/CourseProject/blob/main/arch.drawio.png)

The overall system has two main components (As depicted by the dotted lines).


**Offline Component:**

- As an offline mechanism, we scrape the tweets for the required brands using `twint`. We ensure that we scrape all the replies from the required usenames of the brands.
- We clean the tweets to remove PII and redundency.
- The scraped tweet corpus is embedded in the vector space using sentence transformer. we use `multi-qa-mpnet-base-dot-v1` as the pretrained model to encode our sentence. 
- The embeddings are indexed in the vector space indexer `annoy`.


**Online Component:**

- The user enters a new query. 
- The query is cleaned in the same fashion as the offline mechanism.
- The text data is now embedded in vector space by using sentence transformer. we use `multi-qa-mpnet-base-dot-v1` as the pretrained model to encode our sentence.
- The encoded data is queried in `annoy` to find the nearest neighbour in the vector/embedded space.
- Show the nearest queried tweets.

# Streamlit (UI Component):

We build a simple UI for the users to interact with the tool in a easy mechanism. The UI allows users to:
* Select few pre-chosen brands (Pampers, Tide and Gillette) on the left hand sidebar.
* Use the slider to select how many response/matching tweets they would like to see (on left hand sidebar).
* Few preselected queries for the user to get started quickly and view the system. (on the center pane - 1st dialog box).
* Enter a custom query that the user wished to provide. (on the center pane - 2nd dialog box).

# Evaluation: 
We let a random group of 10 users tests the whole system. Each user attempted to try 5 user queries and rated it on a 10 point scale on how accurate they felt that the results. This mechanism provided a qualitative feedback to the whole system. We get an aggregrated opinion score of 7.3. 

