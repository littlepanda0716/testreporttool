#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:34:32 2021

@author: imclumsypanda
"""
import streamlit as st
from PIL import Image

st.title(':computer:  测试报告工具')
nl=[5,8,3]
for j in range (3):
    with st.beta_expander('测试指标 '+str(j+1),expanded=True):
        cl1=[]
        for i in range(nl[j]):
            if not st.checkbox('测试指标 '+str(j+1)+'.'+str(i+1)+' xxx 符合测试要求',value=True,key=i):
                k=st.number_input('输入issue个数',min_value=0,value=1,step=1,key=(i+1)*1000)
                for ki in range(k):
                    st.text_input('填写issue '+str(j+1)+'.'+str(i+1)+'.'+str(ki+1)+' 名称',key=(i+1)*1000+ki*100+1)
                    st.text_area('填写issue '+str(j+1)+'.'+str(i+1)+'.'+str(ki+1)+' 描述',key=(i+1)*1000+ki*100+1)
                    pics=st.file_uploader('上传issue '+str(j+1)+'.'+str(i+1)+'.'+str(ki+1)+' 对应图片',type=None,accept_multiple_files=True,key=(i+1)*1000+ki*100+1)
                    if len(pics)>0:
                        for picindex,pic in enumerate(pics):
                            image1 = Image.open(pic)
                            st.image(image1,caption='issue '+str(j+1)+'.'+str(i+1)+'.'+str(ki+1)+' 配图 '+str(picindex+1),use_column_width=True)
            
