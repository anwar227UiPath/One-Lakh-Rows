import pandas as pd
import time

def read_excel(file_path):

    start = time.perf_counter()

    df = pd.read_excel(file_path)

    end = time.perf_counter()

    return "welcome"