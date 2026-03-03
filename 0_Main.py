import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn as sk
import streamlit as st

# from yolo import img_infer
# from yolo import vid_infer

sb.set()

#Visualization with Streamlit (Navigation on pages)
pg_1 = st.Page("1_intro.py", title="Introduction", icon ="🏠", default=True)
pg_2 = st.Page("2_stats.py", title="Statistics", icon ="📈")
pg_3 = st.Page("3_infer.py", title="Inference", icon ="🎥")
pg = st.navigation([pg_1, pg_2, pg_3])
pg.run()