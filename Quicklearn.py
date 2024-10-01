#Quicklearn

import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain.tools import Tool
from langchain_groq import ChatGroq
import json
import nest_asyncio
import os

nest_asyncio.apply()

API_KEY = "AIzaSyASpU0qAf8xcDgZ6Wqdw-Ts8WJftF0cDFU"
GROQ_API_KEY = "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"
HUGGINGFACEHUB_API_TOKEN = "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"

def ytsearch(search_query):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    try:
        search_response = youtube.search().list(
            q=search_query,
            part='id,snippet',
            maxResults=2,
            type='video'
        ).execute()

        video_details = [{
            'videoId': item['id']['videoId'],
            'title': item['snippet']['title'],
            'channelTitle': item['snippet']['channelTitle']
        } for item in search_response['items']]

        transcriptions = []
        for video in video_details:
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video['videoId'])
                transcriptions.append({
                    'title': video['title'],
                    'channelTitle': video['channelTitle'],
                    'transcript': transcript
                })
            except Exception as e:
                print(f"An error occurred while retrieving the transcript for video {video['videoId']}: {e}")
                transcriptions.append({
                    'title': video['title'],
                    'channelTitle': video['channelTitle'],
                    'transcript': None
                })

        video1_transcript = ""
        video2_transcript = ""

        if transcriptions[0]['transcript'] is not None:
            video1_transcript = " ".join([line['text'] for line in transcriptions[0]['transcript']])

        if len(transcriptions) > 1 and transcriptions[1]['transcript'] is not None:
            video2_transcript = " ".join([line['text'] for line in transcriptions[1]['transcript']])

        return video1_transcript, video2_transcript, video_details

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return None, None, []

def process_transcript_and_query(transcript, query):
    model_name = "BAAI/bge-base-en-v1.5"
    huggingfacehub_api_token = HUGGINGFACEHUB_API_TOKEN

    docs = [{'page_content': transcript}]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=20)
    chunks = text_splitter.split_documents(docs)

    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=HUGGINGFACEHUB_API_TOKEN, model_name=model_name
    )

    vectorstore = Chroma.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={'k': 2}
    )

    llm = HuggingFaceHub(
        repo_id="huggingfaceh4/zephyr-7b-alpha",
        model_kwargs={"temperature": 0.5, "max_length": 64, "max_new_tokens": 512},
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="refine", retriever=retriever)
    response = qa.run(query)
    return response

def process(search_query):
    global video_transcript1, video_transcript2
    video_transcript1, video_transcript2, video_details = ytsearch(search_query)

    if not video_details:
        st.error("No video details found. Please try a different query.")
        return

    query = f"provide 10 questions on {search_query}"

    process_pdf_and_query_tool1 = Tool(
        name='Process PDF and Query 1',
        func=lambda q: process_transcript_and_query(video_transcript1, q),
        description="Useful for processing a transcript and answering a query based on its contents."
    )

    process_pdf_and_query_tool2 = Tool(
        name='Process PDF and Query 2',
        func=lambda q: process_transcript_and_query(video_transcript2, q),
        description="Useful for processing a transcript and answering a query based on its contents."
    )

    tools = [process_pdf_and_query_tool1, process_pdf_and_query_tool2]

    llm = ChatGroq(model="llama3-8b-8192", groq_api_key=GROQ_API_KEY)
    chat = ChatGroq(model="mixtral-8x7b-32768", groq_api_key=GROQ_API_KEY)

    system_message = "You are a helpful assistant."
    human_message = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system_message), ("human", human_message)])

    chain = prompt | chat
    questions = chain.invoke({"text": query}).content

    tool_query = f"""
    Use the provided tools to answer the following ten questions about {search_query}. For each question, identify and specify the best tool to use. Provide the response in the following format:

    The best tool for [Question] is [Tool Name].

    Only provide the answers in this format, without any additional information or explanations.

    {questions}
    """

    llm_with_tools = llm.bind_tools(tools)
    answers = llm_with_tools.invoke(tool_query).content

    final_query = f"give one word answer which is better query1 or query2. Expected output: query1 or query2 {answers}"
    final_answer = chat.invoke(final_query).content.strip()

    if final_answer == "query1":
        result = video_details[0]
    else:
        result = video_details[1]

    
    opid=result['videoId']
    st.video(f"https://www.youtube.com/watch?v={opid}")


            
            






