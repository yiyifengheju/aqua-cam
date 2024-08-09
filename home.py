"""
=========================================================================
@File Name: home.py
@Time: 2024/5/13 上午2:39
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""
import streamlit as st

from config import INIT


def page_init():
    st.set_page_config(
        page_title="koko-Tools",
        page_icon="🦀",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            # 'Get Help': 'https://www.extremelycoolapp.com/help',
            # 'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "#### Koko-Tools"
        }
    )
    st.title('🦀 Koko-Tools')
    st.caption(INIT.AUTHOR)
    st.markdown(
        """
        <style>

        </style>
        """,
        unsafe_allow_html=True
    )


def page_main():
    st.page_link("pages/1_🍅_RAF重命名.py", label="RAF重命名", icon="🍅")
    st.page_link("pages/2_🍭_压缩Webp.py", label="压缩Webp", icon="🍭")
    st.page_link("pages/3_🍿_图片水印.py", label="图片水印", icon="🍿")


if __name__ == '__main__':
    page_init()
    page_main()
