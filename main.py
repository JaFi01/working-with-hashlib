import hashlib
import timeit
import plotly.graph_objects as go


def hash_time_visualization(phrase: str):
    """Functions which checks how long each alghoritm from hashlib will need to encrypt phrase

    Args:
        phrase (str): input made by user
    """
    algorithms = hashlib.algorithms_available
    times = []
    algorithm_names = []

    for algorithm in algorithms:
        start_time = timeit.default_timer()
        h = hashlib.new(algorithm)
        h.update(phrase.encode())
        end_time = timeit.default_timer()
        hash_time = end_time - start_time
        times.append(hash_time)
        algorithm_names.append(algorithm)
        print(f"Algorithm: {algorithm}, Time: {hash_time:.7f}")

    fig = go.Figure(data=go.Bar(x=algorithm_names, y=times))
    fig.update_layout(title="Time needed for encryption for each algorithm",
                      xaxis_title="algorithm",
                      yaxis_title="time (s)")
    fig.show()

if __name__ == "__main__":
    while(True):
        phrase=""
        phrase = str(input("Please input word, to run all encrypting algorithms\n [input nothing to stop the script]\n"))
        if phrase == "":
            break
        hash_time_visualization(phrase)