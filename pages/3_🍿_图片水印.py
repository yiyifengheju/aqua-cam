"""
=========================================================================
@File Name: 3_🍿_图片水印.py
@Time: 2024/5/31 上午1:19
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""
import os

import streamlit as st
from config import INIT


from koko_learn.PicTools import WaterMarkClass


def page_init():
    st.set_page_config(
        page_title="图片水印",
        page_icon="🍿",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            # 'Get Help': 'https://www.extremelycoolapp.com/help',
            # 'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': f"### 🍿图片水印 \n\n {INIT.AUTHOR}"
        }
    )
    st.title('🍿图片水印')
    st.caption(INIT.AUTHOR)


def page_main():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image('./images/DSCF9285.webp',
                 caption='样式 0')
    with col2:
        st.image('./images/DSCF9304.webp',
                 caption='样式 1')
    with col3:
        st.image('./images/DSCF9302.webp',
                 caption='样式 2')
    with col4:
        st.image('./images/DSCF9307.webp',
                 caption='样式 3')

    st.markdown('---')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        limit_size = st.text_input('限制大小/kb',
                                   key='limit_size',
                                   value='500'
                                   )
    st.markdown('')
    with col2:
        limit_width = st.text_input('限制宽度/px',
                                    key='limit_width',
                                    value='2560'
                                    )
    with col3:
        style_idx = st.selectbox("水印样式",
                                 ('0', '1', '2', '3'),
                                 index=1,
                                 key='style_idx'
                                 )
    with col4:
        cam_make = st.selectbox('相机品牌',
                                ('FujiFilm', 'SONY'),
                                index=0,
                                key='cam_make'
                                )
    col1, col2 = st.columns(2)
    with col1:
        img_src = st.text_input('图片路径',
                                key='img_src'
                                )

    if st.button('生成水印', key='img_btn'):
        if img_src:
            tmp = os.path.abspath(os.path.join(img_src, os.pardir))
            img_dst = f'{tmp}/3_MARKER'
            if not os.path.exists(img_dst):
                os.mkdir(img_dst)

            with st.spinner('等待进程...'):
                wm = WaterMarkClass(path_src=img_src,
                                    path_dst=img_dst,
                                    aim_size=eval(limit_size),
                                    aim_width=eval(limit_width),
                                    style_idx=eval(style_idx),
                                    camera_make=cam_make,
                                    init_info=None,
                                    max_workers=INIT.MAX_WORKERS
                                    )
                # info = wm.run()
                wm.run()
                info = ''
                st.success('压缩完成！')
                with st.expander("压缩信息"):
                    st.write(info)


if __name__ == '__main__':
    page_init()
    page_main()
