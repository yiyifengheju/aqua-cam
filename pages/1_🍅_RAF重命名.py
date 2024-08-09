"""
=========================================================================
@File Name: 1_🍅_RAF重命名.py
@Time: 2024/5/31 上午12:45
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 🍅
- 
=========================================================================
"""
import os

import streamlit as st
from config import INIT

from koko_learn.PicTools import raf_renamer


def page_init():
    st.set_page_config(
        page_title="RAF重命名",
        page_icon="🍅",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            # 'Get Help': 'https://www.extremelycoolapp.com/help',
            # 'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': f"### 🍅RAF重命名 \n\n {INIT.AUTHOR}"
        }
    )
    st.title('🍅 RAF重命名')
    st.caption(INIT.AUTHOR)


def page_main():
    col1, col2 = st.columns(2)
    col3, col4, _, _, _ = st.columns(5)
    with col1:
        raf_src = st.text_input('RAF源路径',
                                key='raf_src'
                                )

        raf_dst = st.text_input('RAF目标路径',
                                value=r'H:\RAF_TMP',
                                key='raf_dst'
                                )
        aim_model = st.text_input('目标相机Model',
                                  value='',
                                  key='aim_model'
                                  )
    with col3:
        if st.button('重命名RAF', key='raf_btn'):
            if raf_src and raf_dst:
                with st.spinner('等待进程...'):
                    raf_renamer(raf_src, raf_dst, aim_model)
                    st.success('重命名完成！')

    with col4:
        if st.button("打开文件路径"):
            os.startfile(raf_dst)


if __name__ == '__main__':
    page_init()
    page_main()
