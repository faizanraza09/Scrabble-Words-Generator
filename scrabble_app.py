import streamlit as st
import pandas as pd


def getwordlist():
    WORD_LIST = "sowpods.txt"
    wordlist = open(WORD_LIST).readlines()
    # Get rid of newlines
    wordlist = set([word.lower().strip() for word in wordlist])
    return wordlist

wordlist=getwordlist()


scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


def anagrams_helper(lst):
    if len(lst)==1 or len(lst)==0:
        return lst
    else:
        letter=lst.pop()
        old=anagrams_helper(lst)
        new=old.copy()
        new.append(letter)
        for i in range(len(old)):
            for j in range(len(old[i])):
                new.append(old[i][:j]+letter+old[i][j:])
            new.append(old[i]+letter)
        return new

def anagrams(letters):
    lst = [word for word in anagrams_helper([i.lower() for i in letters]) if word in wordlist]
    points=[]
    for i in lst:
        temp=0
        for j in i:
            temp+=scores[j]
        points.append(temp)
    ans=dict(zip(lst,points))
    ans= sorted(ans.items(),key=lambda x:x[1],reverse=True)
    return pd.DataFrame.from_records(ans,columns=['Word','Score Obtained'])


if __name__=='__main__':
    st.title('Scrabble Word Generator')
    rack=st.text_input('Enter your rack of letters: ',max_chars=8)
    if st.button('Submit') or rack:
        st.dataframe(anagrams(rack))
