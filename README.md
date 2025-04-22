# streamlit-test
conda create -n streamlit python=3.11
conda activate streamlit
touch app.py
pip install streamlit
streamlit run app.py
pip install pipreqs
pipreqs