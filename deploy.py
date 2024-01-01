import os
import uvicorn
import warnings
warnings.filterwarnings('ignore')

class App:
    ...

app = App()

if __name__ == "__main__":
        uvicorn.run("main:app", host="127.0.0.1", port=36001)
