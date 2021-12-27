import streamlit as st
import processor
import helper
import matplotlib.pyplot as plt


st.sidebar.title("Data Analysis")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    #bytes_data = uploaded_file.getvalue()
    #data = bytes_data.decode("utf-8")
    df = processor.process(uploaded_file)
    
    #st.dataframe(df)
    
    user_list = ['Personal']
    #user_list.remove('group_notification')
    #user_list.sort()
    user_list.insert(0,"Select")
    selected_user = st.sidebar.selectbox("Show Analysis", user_list)


    if st.sidebar.button("Show Analysis"):
        
        if selected_user == "Personal":
            
            st.title("Top Statistics")
            st.title(" ")
            
            Total_cus,Unique_cus,Total_model,Total_wedding= helper.fetch_stats(selected_user,df)
            col1,col2,col3,col4 =  st.columns(4)
        

            with col1:
                original_title = '<p style="font-family:Berlin Sans FB;bold:True; font-size: 30px;">Total customer</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                st.title(Total_cus)
            
            with col2:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Unique customer</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                st.title(Unique_cus)
            
            with col3:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Total modeling</p>'
                st.markdown(original_title, unsafe_allow_html=True)            
                st.title(Total_model)
            
            with col4:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Total wedding</p>'
                st.markdown(original_title, unsafe_allow_html=True)            
                st.title(Total_wedding)
            
            
        if selected_user == "Personal":
            
            Total_Xerox,Total_Karizma,Total_Id,Total_Earning =  helper.fetch_stats_1(selected_user,df)
            col11,col22,col33,col44 =  st.columns(4)
            
            with col11:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Total Xerox/Print</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                st.title(Total_Xerox)
            
            with col22:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Total Kz album</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                st.title(Total_Karizma)
            
            with col33:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Total Id Photo</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                st.title(Total_Id)
            
            with col44:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Total Earning</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                st.title(Total_Earning)
            
            
        if selected_user == "Personal":
            st.title(" \n")
            
            st.title("Graphical Visualization")
            st.title("\n")
            
            cola, colb = st.columns(2)
        
        
            with cola:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Overall Growth rate</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                x= helper.fetch_stats_graphs(df)
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color='darkviolet')
                #plt.xticks(color = 'maroon')
                plt.xlabel('Types')
                plt.ylabel('Values')
                st.pyplot(fig)
            
        
            with colb:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Overall Growth Ratio</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                labels, sizes, explode = helper.fetch_stats_graphs1(df)
                fig, ax = plt.subplots()
                ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
                ax.axis('equal')
                st.pyplot(fig)
            
            
           
        if selected_user == "Personal":
        
            colc, cold = st.columns(2)
        
            with colc:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Agewise Customers</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                x= helper.fetch_stats_graphs2(df)
                fig, ax = plt.subplots()
                ax.plot(x['Age'],x['Amount'], color= 'red')
                plt.xlabel('Age')
                plt.ylabel('Number of customers')
                st.pyplot(fig)
                
        
            with cold:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Monthly Income</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                x= helper.fetch_stats_graphs3(df)
                fig, ax = plt.subplots()
                month = x.index
                amount = x.values
                ax.bar(month, amount,color='green')
                plt.xlabel('Month')
                plt.ylabel('Income')
                st.pyplot(fig)
            
        if selected_user == "Personal":
        
            col5, col6 = st.columns(2)
        
            with col5:
                original_title = '<p style="font-family:Berlin Sans FB; font-size: 30px;">Male vs Female Ratio</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                labels, sizes, explode = helper.fetch_stats_graphs4(df)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90, colors=['forestgreen', 'darkorange'])
                ax1.axis('equal')
                st.pyplot(fig1)
            
            
    
            
            
    
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            