import time


def time_logger(func):
    def inner(*args,**kwargs):
        start = time.time()
        print(f"\n Running {func.__name__}")
        result = func(*args,**kwargs)
        end = time.time()
        elpsed = end - start
        print(f"{func.__name__} finsihed in time {elpsed:.2f}")
        return result
    return inner


@time_logger
def clean_data(text):
    time.sleep(0.5)
    return "data has been cleaned."

@time_logger
def transformData(text,delim):
    time.sleep(0.2)
    return "data has been transformed."

@time_logger
def save_data():
    time.sleep(0.2)
    return "data has been saved..."


def runPipeline(text):
    clean_data("data")
    transformData("data","#")
    save_data()


runPipeline("hi this issamasm   k    knsja   akm m ")       

#cleand data --> extra space remove..
#tite case convert..
#sacve dagta --> print...