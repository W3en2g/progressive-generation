from tqdm.autonotebook import tqdm, trange
import re, os,io, json, time
from IPython.display import clear_output
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

import platform
currPlatform = platform.node()

class Paths():
    def __init__(self, dataset, task = "None"):
        if currPlatform == "LAPTOP-ANCAM179":
            self.basic_folder = "E:/Dataset/story_data/"
            self.data_folder = self.basic_folder + dataset + "/"
            self.output_folder = self.basic_folder + dataset + "/output/"
            self.tool_folder = "D:/Projectach/story_Task/text2events/tool/"
            self.trained_model_folder =self.basic_folder + dataset + task + "/results/"
            # import os
            # os.environ["http_proxy"] = "http://127.0.0.1:7890"
            # os.environ["https_proxy"] = "http://127.0.0.1:7890"

        elif 'container' in currPlatform:
            self.basic_folder = "/root/autodl-tmp/datasets/"
            self.data_folder = self.basic_folder + dataset + "/raw_data/"
            self.output_folder = self.basic_folder + dataset + "/output/"
            self.tool_folder ="/root/autodl-tmp/tool/"
            self.trained_model_folder ="/root/autodl-tmp/trained_model/" + task + "/results/"

        else:
            self.basic_folder = "/content/drive/MyDrive/故事生成/dataset/"
            self.output_folder = "/content/drive/MyDrive/故事生成/output/"
            # enviroment
            import nltk       
            nltk.download('punkt')
            import os 
            os.system("!pip install allennlp==2.1.0 allennlp-models==2.1.0")
            os.system("!pip install git+https://github.com/explosion/spacy-transformers")
            from google.colab import drive
            drive.mount('/content/drive')

    def __str__(self) -> str:
        return ("basic_folder: {};\ndata_folder: {};\noutput_folder: {};\ntool_folder: {};\ntrained_model_folder: {};\n".format(self.basic_folder, self.data_folder, self.output_folder, self.tool_folder, self.trained_model_folder))



