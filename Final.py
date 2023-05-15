from pathlib import Path

import streamlit as st 
from PIL import Image

# path setting #

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css"
resume_file = current_dir / "Assets" / "CV.pdf"
profile_pic = current_dir / "Assets" / "profile.png"
portfolio_file = current_dir / "Assets" / "My_work.pdf"


# general settings #

PAGE_TITLE = " Digital CV | Carlos Vargas"
PAGE_ICON = "👨🏼‍🎨"
NAME = "Carlos Vargas"
DESCRIPTION = "Interdisciplinary artist"

EMAIL = "Vargc12@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/carlos-vargas-a570bb189/",
    "Instagram" : "https://www.instagram.com/dani.media/",
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

# load css, PDF #

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(portfolio_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
Profile_pic = Image.open(profile_pic)

# hero #

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(Profile_pic, width = 230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "Downlaod Resume",
        data= PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream",
    )
    st.download_button(
        label = "Download Portfolio",
        data = PDFbyte,
        file_name = portfolio_file.name,
        mime = "application/octet-stream",
    )   
st.write(EMAIL)

# social Links #
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# experince #

st.write("#")
st.header("Skills")
st.write(
    """
- Well Versed in Adobe Photoshop, Illustrator, InDesign, Premier Pro, and Audition.
- Interdisciplinary artist skilled in traditional mediums and digital art.
- Fluent in Spanish and English speaking.
- Can work well in a fast paced work space.
    """
)

# work History #

st.write("#")
st.header("Work History")
st.write("---")

#--- job 1 #
st.subheader("Studio Assistant")
st.write("2018-2021")
st.write(
    """
    Studio Assistant to abstract painter in the South Bronx. Assisted with production of artwork, goods, and maintenance of studio.
    """
)


#--- job 2 #
st.subheader("ArtsConnection")
st.write("Office Assistant")
st.write("2019-2020")
st.write(
    """
    Organized excel sheets with students name, contact information and art piece data. Clerical work.
    """
)


#--- job 3 #
st.subheader("Parsons Scholar Program ")
st.write("Mentor")
st.write("2019-2023")
st.write(
    """
    Mentor for Highschool sophmores, juniors, and seniors. Assisted in the planning of activities ranging from trip planning to guest artist vistits.
    """
)


#--- job 4 #
st.subheader("ArtsConnection")
st.write("Freelance")
st.write("2020-Current")
st.write(
    """
    Photographer, gallery instalation and planning, art handeling, and art packaging.
    """
)


#--- job 5 #
st.subheader("Artist Assistant")
st.write("2023")
st.write(
    """
    Studio assistant to a soft structure artist.
    """
)













































