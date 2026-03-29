import streamlit as st
import math

st.set_page_config(page_title="Smart Attendance Analyzer", page_icon="📊")

st.title(" Smart Attendance Analyzer")
st.write("Track your attendance and know how many classes you need to attend.")

total_classes = st.number_input("Total classes conducted", min_value=1, step=1)
attended_classes = st.number_input("Classes attended", min_value=0, step=1)

if st.button("Calculate Attendance"):
    
    if attended_classes > total_classes:
        st.error("Attended classes cannot be more than total classes ❌")
    
    else:
        attendance = (attended_classes * 100) / total_classes
        
        st.subheader(f"📈 Attendance: {attendance:.2f}%")
        
        if attendance >= 75:
            st.success("You are safe ")
    
        
        else:
            required_classes = math.ceil((0.75 * total_classes - attended_classes) / 0.25)
            
            st.warning("Attendance is low ⚠️")
            st.write(f"You need to attend next **{required_classes} classes** continuously to reach 75%")

