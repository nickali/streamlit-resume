from pathlib import Path

import streamlit as st
import webbrowser
from PIL import Image
import pandas as pd


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Nick.Ali_Streamlit.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Nick Ali | Steamlit Resume"
PAGE_ICON = ":wave:"
NAME = "Nick Ali"
DESCRIPTION = """
Developer marketer, growth marketer, demand generation, lead generation, developer relations
"""
EMAIL = "n@nali.org"
SOCIAL_MEDIA = {
#    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/nickali/",
#    "GitHub": "https://github.com",
#    "Twitter": "https://twitter.com",
}
PHONE = "(678) 637-7062"

#PROJECTS = {
#    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfN#anQ_9c",
#    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
#}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("☎", PHONE)


# --- SOCIAL LINKS ---
st.write('\n')
#cols = st.columns(len(SOCIAL_MEDIA))
#for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#    cols[index].write(f"[{platform}]({link})")

colLink1, colLink2, colLink3 , colLink4= st.columns(4, gap="small")

linkedinUrl = 'https://www.linkedin.com/in/nickali/'
githubUrl = 'https://github.com'

with colLink1:
    if st.button('LinkedIn'):
        webbrowser.open_new_tab(linkedinUrl)

with colLink2:
    if st.button('Resume Code'):
        webbrowser.open_new_tab(githubUrl)

with colLink3:
    st.write("&nbsp;")

with colLink3:
    st.write("&nbsp;")

    
# --- Summary ---
st.write('\n')
st.write(
    """
    Senior developer-turned-marketer with experience creating and executing marketing strategies encompassing growth marketing, product marketing, and brand marketing. Responsible for accelerating revenue growth by building developer and B2B demand generation and lead generation strategies. Trusted business partner for executive leadership and stakeholders. 
    """
    )

# --- EXPERIENCE & QUALIFICATIONS ---
# --- WORK HISTORY ---
st.write('\n')
st.subheader("Skills")
st.write("---")

d = {

    '✔️ Marketing Strategy': ['✔️Developer Marketing', '✔️Campaign Planning and Execution', '✔️Growth Marketing'], '✔️Product Marketing': [ '✔️Branding and Positioning', '✔️Marketing Operations', '✔️P&L Management'], '✔️Startups, Scaleups, Market Expansion' : ['✔️Mentorship', '✔️Player / Coach', '✔️Team Creation and Expansion']

}

df = pd.DataFrame(data=d)
styler = df.style.hide_index()

st.write(styler.to_html(), unsafe_allow_html=True)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Marketing Work History")
st.write("---")

# --- JOB 1
st.write("**Marketing Advisor | Kuverant**")
st.write("05/2022 - Present")
st.write(
    """
    - ► Consult with clients to evaluate and formulate marketing strategies and go-to-market plans.
    - ► Review market conditions, research competitors, and develop unique value propositions.
    - ► Refine segmentation and sales targets, define MQLs, PQLs, and SQLs in coordination with sales.
    - ► Evaluate campaign effectiveness and identify opportunities for improvement.
    - ► Interview marketing candidates and counsel clients during agency hiring process.
    """
)

# --- JOB 2
st.write('\n')
st.write("**Marketing Director | Tatum**")
st.write("10/2021 - 05/2022")
st.write("""
    Hired by founder and CEO of early stage blockchain developer platform.
"""
         )
st.write(
    """
    - ► Responsible for transforming marketing team to develop and execute more effective marketing initiatives with greater ROI.
    - ► Created and launched go-to-market strategies and user acquisition plan targeting enterprises, startups, and developers.
    - ► Established unique value proposition and product positioning working with business development, product, customer success, and partnership teams.
    - ► Created ICPs and identified user and buyer journeys from brand awareness to referral. Aligned and directed brand and growth campaigns simultaneously for customer acquisition.
    - ► Leveraged technical leadership experience to form developer relations team and support community of developers.
    - ► Delivered 10x growth in signups in first six months by aligning funnel and journey touchpoints with messaging, content, and paid ads.
    - ► Slashed cost per lead by 90% through experimentation, continuous testing, and spend optimization of messaging, creative, content, and ads on all channels.
    - ► Increased web site visitors 200% by creating SEO-optimized content leveraging blog, email marketing, webinars, Twitter, LinkedIn, YouTube, and influencers, all aligned with developer journey.
    - ► Reduced campaign delivery times by 50% through improved talent acquisition, up-skilling of team, and adherence to processes.
    - ► Doubled conversion rate and tripled CTR by improving targeting, retargeting, and development of channel-specific content.
"""
)

# --- JOB 3
st.write('\n')
st.write("**COO | Demmark The Agency**")
st.write("01/2012 - 10/2021")
st.write("""
Guided data-driven creative strategy, planning, and execution of multiple simultaneous short- and long-term omni-channel marketing plans for agency and B2B, B2C, and B2B2C clients.
"""
)

st.write(
    """
    - ► Identified unique value proposition in collaboration with executive teams that drove positioning, goal setting, prioritization, marketing, sales, PR, overall customer experience, and employee engagement.
    - ► Designed growth strategy to maximize LTV and minimize CAC.
    - ► Provided extensive technical subject matter expertise and leadership evaluating and selecting best-of-breed partners to integrate into marketing technology stacks.
    - ► Managed workflow and capacity planning, recruitment, and performance management of team, forming a flexible, collaborative, and responsive culture to meet all client needs.
    - ► Achieved 225% growth in B2B SaaS monthly subscription revenue for national food services client by identifying user personas and journeys, developing effective marketing strategy, and collaborating with partners and affiliates on alignment of messaging, branded content, and sales material.
    - ► Increased employee engagement by 17% at multinational financial through design and execution of impactful internal brand management, educational campaigns, videos, and communications.
    - ► Reduced CAC 20% for global insurance company by improving UX in customer-facing SaaS tool for EMEA region.
    - ► Rebranded largest RPO in US and named new AI-fueled hiring platform. 
"""
)

# --- JOB 4
st.write('\n')
st.write("**CMO | Run Level Media**")
st.write("01/2009 - 01/2012")
st.write("""
Founded marketing agency focused on creating and executing comprehensive marketing strategies, plans, campaigns, and websites. 
"""
)

st.write(
    """
    - ► Leveraged content creation, SEO, social media marketing, paid advertising, A/B testing, and media relations for clients.
    - ► Served as primary technical advisor on all projects, collaborating with strategists, designers, technologists, and third-party freelancers / vendors.
    - ► Designed and built lead generation tools for largest home improvement retailer that allowed customers to input minimal project specifications and receive detailed requirements to use at point of purchase.
    - ► Reduced multinational healthcare website bounce rate by 35% and increased session duration 30% by guiding client through prioritizing product focus and identifying customer segments, developing new marketing and sales strategies, and redesigning website user experience.
    - ► Developed custom marketing platform for top three vehicle rental company, successfully redesigning reservation system front-end experience and integrating with CRM.
    """
    )

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Developer Work History")
st.write("---")


# --- Job 5
st.write('\n')
st.write("**Software Architect | EmployEase (acquired by ADP)**")
st.write("02/2005 - 01/2009")
st.write("""
Transformed enterprise human capital management software-as-a-service (SaaS) application serving millions of users into scalable and highly-available future-proofed platform. Designed foundational architectural changes that facilitated launch of completely distributed platform. Trained developers on new architecture, frameworks, methodologies, and processes.
"""
)

# --- Job 6
st.write('\n')
st.write("**Software Developer | iTendant**")
st.write("08/2001 - 02/2005")
st.write("""
Specialized in development of software solutions focused on energy conservation and sustainability in commercial and institutional sector. Engineered SaaS platform that enabled fast, secure communication and tracking for large, high-quality Class A buildings and hotels. Led design and execution of digital security features, automating account manager implementation, onboarding functions and deploying new software releases and upgrades.
"""
)

# --- Education
st.write('\n')
st.subheader("Education")
st.write("---")


st.write('\n')
st.write("**BS Computer Engineering | Georgia Tech '01 🎓**")

st.write("**Coursera Certificates**")
st.write("""
- ► Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization
- ► Structuring Machine Learning Projects
- ► Neural Networks and Deep Learning
"""
)

st.write("**Udacity Nanodegrees**")
st.write("""
- ► Deep Learning Foundation
- ► Machine Learning
- ► Artificial Intelligence
"""
)
