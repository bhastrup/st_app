
import pandas as pd
import datetime
import numpy as np

from typing import Dict, Tuple, List, Set, Union, Any, cast

import streamlit as st



project_list = [None] + ['SPSA', 
		     'RL for Doom',
		     'MPC for algo bidding',
		     'Model Based Machine Learning for soccer']

st.sidebar.header('Choose project:')
agency = st.sidebar.selectbox('Project', project_list)

# make function that reads project abstracts
