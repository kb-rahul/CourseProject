import re
import streamlit as st
from annoy import AnnoyIndex
import json
from sentence_transformers import SentenceTransformer

@st.cache(allow_output_mutation=True)
def load_data_and_model():
    model_name = 'multi-qa-mpnet-base-dot-v1'
    model = SentenceTransformer(model_name)
    with open("./data/tweets_dump.json", 'r') as fp:
        data_tweets = json.load(fp)
    return model, data_tweets

st.title("Welcome to the Project Application for CS410!")
st.sidebar.subheader("Team Name: NFSMW ")
st.sidebar.subheader("NetID: fnuk2@illinois.edu")
st.sidebar.subheader("Name: Kishan Borule Rahul")

brand = st.sidebar.selectbox("Which brand would you like to search for?", ("Pampers", "Gillette", "Tide"))
num_results = st.sidebar.slider("How many results do you wish to see?", min_value=1, max_value=5, value=3)


if brand == "Pampers":
    defaults = ["My baby's diapers are leaking", "Can my baby act in your advertisements?", "My baby has developed a rash after using your diapers"]
elif brand == "Gillette":
    defaults = ["Gillette is definitely best a man can get!", "I can't find a gillette razor near me, please help.", "Do you have any products for women?"]
else:
    defaults = ["Tide pods have left a stain on my clothes, I don't know how to clean them. Please help!", "I absolutely love your products!", "My kid has accidently ingested tide pod! Please help!"]

selection = st.selectbox("Example queries:", defaults)

query = st.text_input("Please enter your custom query for the brand: {}".format(brand), selection)

embed_size = 768
u = AnnoyIndex(embed_size, 'angular')
u.load('./models/{}.ann'.format(brand.lower())) 
model, data_tweets = load_data_and_model()
emb = model.encode(query, show_progress_bar=False)
indexes = u.get_nns_by_vector(emb, num_results)
results = [re.sub(r"(?:\@)\S+", "", data_tweets[brand][idx].strip()) for idx in indexes]
md_text = ["\n|  | Response Tweets |"]
for idx, result in enumerate(results):
    md_text.append("| - | - |")
    md_text.append("|{}|{}|".format(idx + 1 , result))
st.markdown("\n".join(md_text))

