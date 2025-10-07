import statistics as st

arr = list(map(int, input("Enter numbers: ").split(',')))
mean = st.mean(arr)
median = st.median(arr)
mode = st.mode(arr)
avg = (mean + median + mode) / 3
print("Output:", int(avg))
