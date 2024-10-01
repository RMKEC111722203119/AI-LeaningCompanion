import streamlit as st

# Predefined roadmaps with detailed content (Markdown format for flexibility)
predefined_roadmaps = [
    {
        'title': "Machine Learning Roadmap",
        'author_name': "Vasudevan",
        'author_desc': "Working at amazon, rmkec '24",
        'article_desc': "Structured roadmap covering essential aspects of Machine Learning Process.",
        'content': """
       # Machine Learning Roadmap - My Journey

Welcome to my Machine Learning roadmap! I started my journey as a beginner, just like you, and I want to share the path I took to become proficient in machine learning. Each step below includes videos and resources that helped me along the way.

---

## Overall Machine Learning Process Flowchart
Below is a simple flowchart that visually represents the main steps in the machine learning process:

![ML Flowchart](https://miro.medium.com/max/1400/1*vp_RiS-yPuBr_mS_Uk6SeQ.png)

---

## 1. Introduction to Machine Learning
When I first heard about machine learning, I was fascinated by how computers can learn from data.
- **My Recommendation:** Understand what machine learning is and how it’s shaping the world.
- **Key Lesson:** Machine learning allows computers to learn from data without being explicitly programmed.

Watch the video that helped me understand the basics:

<iframe width="560" height="315" src="https://www.youtube.com/embed/GwIo3gDZCVQ" 
title="Introduction to Machine Learning" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Example of Real-World Machine Learning
![ML Real-World](https://miro.medium.com/max/1400/1*j8sj2FfQ1XftpiCxvvFJbw.png)

---

## 2. Data Preprocessing - The Backbone of ML
As I progressed, I realized that data preprocessing is one of the most crucial steps.
- **My Experience:** Cleaning, transforming, and preparing raw data is critical to making any algorithm work well.
- **Key Lesson:** Without proper data preprocessing, your model won’t perform optimally.

Watch this video to learn how I mastered data preprocessing:

<iframe width="560" height="315" src="https://www.youtube.com/embed/5ueOeyL9w3I" 
title="Data Preprocessing" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Data Preprocessing Example
![Data Preprocessing Example](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Data_preprocessing_steps.png/800px-Data_preprocessing_steps.png)

---

## 3. Feature Engineering - Adding Meaning to Data
In my journey, I discovered that selecting the right features made a significant difference.
- **My Experience:** Feature engineering can be tricky but gives your model the power to succeed.
- **Key Lesson:** Selecting and transforming the right data features improves model performance tremendously.

Check out the video that guided me through feature engineering:

<iframe width="560" height="315" src="https://www.youtube.com/embed/7Z5P9NGn-kE" 
title="Feature Engineering" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Feature Engineering Example
![Feature Engineering Example](https://miro.medium.com/max/1400/1*E-jV2_BuTSBG17dVnCB6QQ.png)

---

## 4. Model Training - Getting into the Real ML
Once you have good data, you’ll need to train your models.
- **My Experience:** Training models was where things started to get exciting. I could see the patterns in data come to life.
- **Key Lesson:** Training models involves feeding data to algorithms so they can learn and make predictions.

Here’s a video that helped me start training models:

<iframe width="560" height="315" src="https://www.youtube.com/embed/MW5OGi1AY6I" 
title="Model Training" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Model Training Visualization
![Model Training Visualization](https://miro.medium.com/max/1200/1*rvFxRrGp-_ZxLqMPX3HfFw.gif)

---

## 5. Model Evaluation - Knowing When You're Right
After training models, I needed to evaluate how good they were.
- **My Experience:** I made sure to evaluate my models using metrics like accuracy, precision, and recall.
- **Key Lesson:** It’s important to assess a model’s performance to ensure it’s making accurate predictions.

Watch this video to learn how I evaluated my models:

<iframe width="560" height="315" src="https://www.youtube.com/embed/oh3FQdYhNQA" 
title="Model Evaluation" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Model Evaluation Metrics
![Model Evaluation](https://miro.medium.com/max/1400/1*RNKjYDPdGhEZYBIVpI8fsA.png)

---

## 6. Model Deployment - Putting it All Together
The last part of my journey was deploying the model to make real-time predictions.
- **My Experience:** I learned how to integrate the model into an application and see it work in the real world.
- **Key Lesson:** Deployment is critical because it brings your model to life and makes it useful for others.

Check out this video to learn more about model deployment:

<iframe width="560" height="315" src="https://www.youtube.com/embed/m6kOIVFC8lw" 
title="Model Deployment" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Model Deployment Diagram
![Model Deployment](https://miro.medium.com/max/1200/1*3pUOLpZsf6RuQ37IYgRL_w.jpeg)

---

### Conclusion
I hope this roadmap gives you a clear understanding of the path I followed to learn machine learning. Stick to it, be consistent, and you’ll find success in this field just like I did!
"""

    },
    {
        'title': "Semiconductor Roadmap",
        'author_name': "Semiconductor Specialist",
        'author_desc': "Good with semiconductors",
        'article_desc': "An insightful roadmap for understanding semiconductor technologies.",
        'content': """
        ## Semiconductor Roadmap
        1. **Physics of Semiconductors**: Band theory, p-n junctions
        2. **Device Fundamentals**: Diodes, transistors (MOSFET, BJT)
        3. **Fabrication Process**: Cleanroom technology, photolithography
        4. **Advanced Topics**: SOI, FinFETs, quantum computing technologies
        """
    },
    {
        'title': "NEET Exam Roadmap",
        'author_name': "Srinivasa Ramanujan",
        'author_desc': "NEET Topper, AIIMS '23",
        'article_desc': "overview of Effective strategies for Neet exam preparation.",
        'content': """
       # NEET Preparation Roadmap - My Journey

Hello, aspiring doctors! I’m excited to share my journey on how I cracked NEET and secured admission to my dream medical college. This roadmap will provide you with key insights, resources, and strategies I used to prepare for NEET. Let’s get started on this challenging but rewarding journey!

---

## Overall NEET Preparation Flowchart
Here's a flowchart to help you understand the overall process of preparing for NEET:

![NEET Prep Flowchart](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Education_flowchart.svg/1920px-Education_flowchart.svg.png)

---

## 1. Understanding the NEET Syllabus & Exam Pattern
The first step is to **understand the NEET syllabus** and the **exam pattern**. NEET focuses on three subjects: Physics, Chemistry, and Biology.
- **My Tip:** Familiarize yourself with the weightage of each chapter.
- **Key Lesson:** Biology (Zoology + Botany) makes up 50% of the exam, while Physics and Chemistry have equal weightage.

### NEET Exam Pattern
- **Total Questions:** 200 (180 to be answered)
- **Total Marks:** 720
- **Subjects:** Physics, Chemistry, Biology

Here’s a helpful video that explains the syllabus and exam pattern in detail:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Y0rHS51gnl4" 
title="NEET Syllabus & Exam Pattern" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## 2. Building Strong Fundamentals - NCERT Books
NEET preparation starts with **NCERT textbooks** for Physics, Chemistry, and Biology. These books form the foundation of your NEET journey.
- **My Experience:** I focused on revising each chapter thoroughly from NCERT and making notes for quick revision.
- **Key Lesson:** Many questions in NEET come directly from NCERT.

Here’s how I used NCERT effectively:

<iframe width="560" height="315" src="https://www.youtube.com/embed/T5t88TohK8I" 
title="How to Study NCERT for NEET" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Example of NCERT Physics Concepts
![NCERT Physics Example](https://physicscatalyst.com/jee/wp-content/uploads/2020/04/NCERT-Physics-Building-Fundamentals.jpg)

---

## 3. Practice, Practice, and More Practice - Solving Mock Tests
After building strong fundamentals, it's crucial to **solve mock tests** and **practice previous year question papers**. This helps in understanding the question pattern and managing time during the exam.
- **My Experience:** I solved at least one mock test daily in the last 3 months before the exam.
- **Key Lesson:** Time management is crucial in NEET, and regular practice helps improve speed and accuracy.

Watch this video for tips on solving mock tests:

<iframe width="560" height="315" src="https://www.youtube.com/embed/vCxowLMIrX4" 
title="How to Solve NEET Mock Tests" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Sample of NEET Mock Test Strategy
![NEET Mock Test Strategy](https://i.ytimg.com/vi/g2aTZhkv7SY/maxresdefault.jpg)

---

## 4. Focused Subject-Wise Preparation
Next, I focused on each subject individually to strengthen weak areas and improve my overall performance:
- **Biology:** Focus on NCERT diagrams and theory.
- **Physics:** Solve conceptual and numerical problems.
- **Chemistry:** Divide attention between Physical, Organic, and Inorganic Chemistry.

### Detailed Subject-Wise Plan:
- **Physics:** Emphasize problem-solving and formulas.
- **Chemistry:** Break down chapters into Physical, Organic, and Inorganic sections.
- **Biology:** Make sure to memorize important facts and diagrams.

Here's a subject-wise NEET strategy video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZcxZB3ZwR5s" 
title="Subject-wise NEET Preparation Strategy" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## 5. Time Management & Study Schedule
Time management was critical to my preparation. I created a daily and weekly schedule that balanced all three subjects and allowed time for revision and mock tests.
- **My Tip:** Dedicate 6-8 hours per day to focused study, with regular breaks.
- **Key Lesson:** Consistency is the key. Stick to your schedule.

Here’s a helpful video on creating an effective study plan:

<iframe width="560" height="315" src="https://www.youtube.com/embed/dKwRDb4I7QU" 
title="NEET Study Schedule" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### NEET Study Plan Example
![NEET Study Plan](https://i.ytimg.com/vi/_ZPj0nFp8_Q/maxresdefault.jpg)

---

## 6. Revision and Doubt Clearing
In the last few months before NEET, I focused on **revision** and **clearing doubts**. Revising regularly and revisiting difficult topics helped solidify my preparation.
- **My Experience:** I used flashcards for quick revision and joined a coaching center for doubt-clearing sessions.
- **Key Lesson:** The last 1-2 months before the exam are crucial for revision.

This video provides revision techniques for NEET:

<iframe width="560" height="315" src="https://www.youtube.com/embed/wT-0HK1KjXE" 
title="NEET Revision Strategy" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Sample of Flashcards for NEET Revision
![Flashcards for NEET Revision](https://cdn.shopify.com/s/files/1/0047/8407/7092/products/Flashcards_Physics_Half_01_1500x.jpg)

---

## 7. Mental Preparation & Exam Day Strategy
The day of the exam can be stressful. I worked on staying calm and confident, and I had a clear strategy for attempting the paper.
- **My Experience:** I started with the Biology section, which is my strength, then moved to Chemistry, and finished with Physics.
- **Key Lesson:** Managing stress and time on exam day is crucial.

Watch this video for exam day tips:

<iframe width="560" height="315" src="https://www.youtube.com/embed/F0ghdLE97sI" 
title="NEET Exam Day Strategy" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Conclusion
That’s my NEET preparation roadmap! Following these steps, staying consistent, and putting in the effort will surely help you achieve success. Good luck, and remember – hard work pays off!
"""
    }
]

def init_state():
    # Initialize session state for articles if not already present
    if 'articles' not in st.session_state:
        st.session_state['articles'] = predefined_roadmaps[:]  # Start with predefined roadmaps

    # Initialize session state for likes and comments
    if 'likes' not in st.session_state:
        st.session_state['likes'] = [0] * len(st.session_state['articles'])  # Zero likes initially
    if 'comments' not in st.session_state:
        st.session_state['comments'] = [[] for _ in range(len(st.session_state['articles']))]  # Empty comments initially

def display_feed_item(title, author_name, author_desc, article_desc, article_id):
    st.markdown(f"### {title}")
    st.markdown(f"**Author**: {author_name}")
    st.markdown(f"**About the Author**: {author_desc}")
    st.markdown(f"**Description**: {article_desc}")
    
    # Read Roadmap link
    if st.button(f"Read Roadmap", key=f"read_roadmap_{article_id}"):
        st.session_state['current_page'] = "article"
        st.session_state['current_article_id'] = article_id

    # Like button
    if st.button(f"👍 Like ({st.session_state['likes'][article_id]})", key=f"like_{article_id}"):
        st.session_state['likes'][article_id] += 1

    # Comment section
    with st.expander(f"💬 Comments ({len(st.session_state['comments'][article_id])})"):
        for comment in st.session_state['comments'][article_id]:
            st.markdown(f"- {comment}")
        new_comment = st.text_input(f"Add a comment for {title}", key=f"comment_input_{article_id}")
        if st.button(f"Submit Comment for {title}", key=f"submit_comment_{article_id}"):
            if new_comment:
                st.session_state['comments'][article_id].append(new_comment)
                st.success(f"Comment added to {title}!")

def display_full_article(article):
    st.markdown(f"## {article['title']}")
    st.markdown(article['content'], unsafe_allow_html=True)  # Allow Markdown & HTML rendering

def add_new_article():
    st.subheader("Add a New Article")
    
    title = st.text_input("Article Title", key="new_article_title")
    author_name = st.text_input("Author Name", key="new_article_author_name")
    author_desc = st.text_area("Author Description", key="new_article_author_desc")
    article_desc = st.text_area("Article Description", key="new_article_article_desc")
    content = st.text_area("Complete Article Content (Markdown Supported)", key="new_article_content")

    if st.button("Submit Article", key="submit_article"):
        if title and author_name and author_desc and article_desc and content:
            article = {
                'title': title,
                'author_name': author_name,
                'author_desc': author_desc,
                'article_desc': article_desc,
                'content': content
            }
            predefined_roadmaps.append(article)  # Add the new article to the predefined list
            st.session_state['articles'].append(article)
            st.session_state['likes'].append(0)  # Add a like count for the new article
            st.session_state['comments'].append([])  # Add a comment list for the new article
            st.success("Article added to All Feeds!")
        else:
            st.error("Please fill in all the fields.")

def run_feed():
    # Main page logic
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = "Home"
        st.session_state['current_article_id'] = None

    if st.session_state['current_page'] == "Home":
        st.header("🎓 - All Roadmaps")
        st.markdown("")

        # Display all articles (predefined + user-added) in a single feed column-wise
        col1, col2 = st.columns(2)
        
        for idx, article in enumerate(st.session_state['articles']):
            if idx % 2 == 0:  # Display in first column
                with col1:
                    display_feed_item(
                        title=article.get('title', 'No Title'),
                        author_name=article.get('author_name', 'Unknown Author'),
                        author_desc=article.get('author_desc', 'No Description'),
                        article_desc=article.get('article_desc', 'No Description'),
                        article_id=idx
                    )
            else:  # Display in second column
                with col2:
                    display_feed_item(
                        title=article.get('title', 'No Title'),
                        author_name=article.get('author_name', 'Unknown Author'),
                        author_desc=article.get('author_desc', 'No Description'),
                        article_desc=article.get('article_desc', 'No Description'),
                        article_id=idx
                    )
        add_new_article()

    elif st.session_state['current_page'] == "article":
        article_id = st.session_state['current_article_id']
        article = st.session_state['articles'][article_id]
        display_full_article(article)

        # Button to return to All Feeds
        if st.button("Back to All Feeds"):
            st.session_state['current_page'] = "Home"
