{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "30e6cfb7-1d94-4024-9185-ab7ccfca208c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-11-25 12:39:02.358 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python\n",
    "# coding: utf-8\n",
    "\n",
    "# In[ ]:\n",
    "\n",
    "\n",
    "import streamlit as st\n",
    "import pickle\n",
    "import pandas as pd\n",
    "\n",
    "def recommend(movie):\n",
    "    movie_index = movies[movies['title'] == movie].index[0] \n",
    "    distances = similarity[movie_index]\n",
    "    movie_list = sorted(list(enumerate( distances)),reverse =True , key = lambda x:x[1])[1:6]\n",
    "    \n",
    "    recommended_movies = []\n",
    "    \n",
    "    for i in movie_list:\n",
    "        recommended_movies.append(movies.iloc[i[0]].title)\n",
    "    return recommended_movies\n",
    "        \n",
    "movies_dict = pickle.load(open('movies_dict.pkl','rb'))\n",
    "movies = pd.DataFrame(movies_dict)\n",
    "\n",
    "similarity = pickle.load(open('similarity.pkl','rb'))\n",
    "\n",
    "st.title('Movie Recommender System')\n",
    "\n",
    "option = st.selectbox('Slect your Movie:', movies['title'].values)\n",
    "\n",
    "if st.button('Recommend'):\n",
    "    recommendations = recommend(option)\n",
    "    for i in recommendations:\n",
    "        st.write(i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6fd100e4-a1da-463a-b86d-dae269923046",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2781496354.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[2], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run app.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "\n",
    "streamlit run app.py"
   ]
  },
  {
   "cell_type": "code",
   "id": "7d5411a4-ecac-446b-8d5b-cd469a6271ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
