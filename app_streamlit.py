import streamlit as st 
# from st_pages import hide_pages
# from streamlit_extras.switch_page_button import switch_page
from PyPDF2 import PdfReader
import json
import yake
kw_extractor = yake.KeywordExtractor()
from transformers import AutoModelForSeq2SeqLM , AutoTokenizer , T5TokenizerFast


## background: radial-gradient(ellipse at 84% 0%,#FF0037, rgba(208, 52, 86, 1), rgba(189, 60, 88, 1), rgba(255, 135, 161, 1))

page_bg_img = """
<style> 
[data-testid='stAppViewContainer']{
}</style>
"""
# job_title = "Senior Java Developer"
# preferred_qualification = "3+ years of Java, Spring Boot"
# hiring_company_name = "Google"
# user_name = "Emily Evans"
# past_working_experience= "Java Developer at google for 4 years"
# current_working_experience = "Senior Java Developer at ABC for 1 year"
# skilleset= "Java, Spring Boot, Microservices, SQL, AWS"
# qualification = "Master's in Electronics Science"

def find_and_comma_separate_next_words(string, target_word, num_words=40):
    # Split the string into words
    words = string.split()
    next_words = []

    # Iterate through words to find the target word
    for i in range(len(words)):
        # Check if the current word matches the target word (case insensitive)
       if words[i].lower() in [target_word.lower() for target_word in target_words]:
            # Store the next num_words words after the target word in a list
            next_words = words[i + 1: i + num_words + 1]
            break  # Exit the loop after storing the words

    # Join the next_words list using commas
    comma_separated_words = ' '.join(next_words)

    print(type(comma_separated_words))
    comma_separated_words = comma_separated_words.replace('.', ",")
    comma_separated_words = comma_separated_words.replace(':', ",")
    # comma_separated_words = comma_separated_words.replace(',', ", ")
    return comma_separated_words.split(', ')

general_skills = [
    "Microsoft Excel",
    "Microsoft PowerPoint",
    "Microsoft Office",
    "Communication Skills",
    "Problem-Solving Skills",
    "Time Management",
    "Teamwork",
    "Leadership",
    "Critical Thinking",
    "Adaptability",
    "Creativity",
    "Analytical Skills",
    "Presentation Skills",
    "Project Management",
    "Customer Service",
    "Research Skills",
    "Performance marketing",
    "evaluate",
    "analyse",
    "reporting"

]

data_science_skills = [
    "Python",
    "R",
    "SQL",
    "Java",
    "Scala",
    "Descriptive Statistics",
    "Inferential Statistics",
    "Hypothesis Testing",
    "Regression Analysis",
    "Time Series Analysis",
    "Supervised Learning",
    "Unsupervised Learning",
    "Ensemble Methods",
    "Neural Networks",
    "Machine Learning Algorithms",
    "Data Extraction",
    "Data Cleaning",
    "Data Transformation",
    "Data Integration",
    "Matplotlib",
    "Seaborn",
    "Plotly",
    "Tableau",
    "Power BI",
    "Data Dashboarding",
    "Hadoop",
    "Spark",
    "Hive",
    "Kafka",
    "HBase",
    "Relational Databases",
    "NoSQL Databases",
    "Git",
    "GitHub",
    "GitLab",
    "Amazon Web Services (AWS)",
    "Microsoft Azure",
    "Google Cloud Platform (GCP)",
    "Text Preprocessing",
    "Text Tokenization",
    "Sentiment Analysis",
    "Named Entity Recognition (NER)",
    "Topic Modeling",
    "Text Classification",
    "ETL Processes",
    "Data Pipelines",
    "Data Warehousing",
    "Data Lakes",
    "Data analysis",
    "Data Analytics",
    "LLM",
    "GPTs",
    "Large Language Models"
]

computer_science_skills = [
    "Arrays",
    "Linked Lists",
    "Stacks",
    "Queues",
    "Trees",
    "Graphs",
    "Hash Tables",
    "Sorting Algorithms",
    "Searching Algorithms",
    "Dynamic Programming",
    "Greedy Algorithms",
    "Graph Algorithms",
    "Object-Oriented Programming (OOP)",
    "Design Patterns",
    "Software Testing",
    "Software Development Life Cycle (SDLC)",
    "Linux/Unix",
    "Windows",
    "Shell Scripting",
    "Parallel Computing",
    "Distributed Computing",
    "Cluster Computing",
    "TCP/IP Protocols",
    "Network Security",
    "Routing and Switching",
    "HTML",
    "CSS",
    "JavaScript",
    "Web Frameworks",
    "RESTful APIs",
    "Threat Detection",
    "Encryption",
    "Penetration Testing",
    "Security Policies",
    "GDPR Compliance",
    "Data Anonymization",
    "Ethical Data Handling",
    "Linear Algebra",
    "Calculus",
    "Probability and Statistics"
]

# Combine all lists into a single list
all_skills = general_skills + data_science_skills + computer_science_skills





tokenizer = AutoTokenizer.from_pretrained('t5-small')

# tokenizer = T5TokenizerFast.from_pretrained('t5-small')

new_session = False

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def new_func():
    st.session_state.clicked = True


def get_pdf_text(file):
    text = ""
    pdf_reader = PdfReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
    

st.markdown(page_bg_img , unsafe_allow_html = True)
st.title('WriteRight')
st.text('AI-Powered Cover Letter Composer')

jd_data = st.text_area("",placeholder = 'Enter or Copy/Paste Job Description', height = 250)

if jd_data :
    st.button("Next >> ", type="secondary",  on_click = new_func )
    if st.session_state.clicked:
        st.markdown('### **Upload your Resume**')
        file = st.file_uploader('')
        if file : 
            resume_data = get_pdf_text(file)
            target_words = ["skill", "skills"]
            skilleset = find_and_comma_separate_next_words(resume_data, target_words)
            keywords = kw_extractor.extract_keywords(jd_data)
            matching_skills = []
            for search_string in keywords:
                if any(search_string[0].lower() in skill.lower() for skill in all_skills):
                    matching_skills.append(search_string[0])
            st.write("For Personalized Cover Letter , mention the below :")
            col1, col2 = st.columns(2)
            with col1:
                job_title = st.text_input(
                    "Enter the job title ",
                    key="placeholder1",
                )
                job_company = st.text_input(
                    "Enter the Company Name ",
                    key="placeholder2",
                )
            with col2:
                qualification = st.text_input(
                    "Enter your Education",
                    key="placeholder4",
                )
                
            # experience = ""
            # username = '[Your Name]'
            press = st.button('Generate', type = "primary")
            if press:
                if  job_title == "":
                    job_title = "ABC role"
                if job_company == "":
                    job_company = "XYZ company"
                if qualification == "":
                    qualification = "Bachelor's in Technology"
                input_text = f"Role: {job_title},\n" \
                f"Qualifications: {matching_skills},\n" \
                f"Company: {job_company},\n" \
                f"Skillsets: {skilleset},\n" \
                f"Qual: {qualification}\n"
                encoded_input = tokenizer.encode(input_text, return_tensors='pt', max_length = 2048, truncation = True)
                model1 = AutoModelForSeq2SeqLM.from_pretrained('./New_modelwithGPU')
                generated_tokens_with_prompt = model1.generate(encoded_input,  max_length=2048 , )
                letter = tokenizer.decode(generated_tokens_with_prompt[0], skip_special_tokens=True)
                st.title("Response:")
                st.write(letter)
            