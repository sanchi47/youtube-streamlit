import streamlit as st
import time


st.title("Streamlit 超入門")

st.write("Display Image")

st.write("プレグレスバーの表示")
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

option = st.select_slider('今の体調を入力してください。',list(range(1,100)))

'あなたの趣味は、', option, 'です'

left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問合せ')
expander.write('問い合わせ内容を書く')

# if st.checkbox('Show Image') :
#     imag = Image.open('friends_hagemasu_businessman.png')
#     st.image(imag,caption='friends_hagemasu',use_container_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )

