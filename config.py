import  os
filt_path = os.path.abspath(__file__)
father_path=os.path.abspath(os.path.dirname(filt_path)+os.path.sep+".")



GPU_ID = 0

#psenet相关
pse_long_size = 640
pse_model_type  = "mobilenetv2"
pse_scale = 4
if  pse_model_type == "mobilenetv2":
    pse_model_path = os.path.join(father_path, "models/psenet_lite_mbv2.pth")
#crnn相关
crnn_type  = "lite_lstm"
if crnn_type == "lite_lstm":
    nh = 256
    LSTMFLAG = True
    crnn_model_path =  os.path.join(father_path,"models/crnn_lite_lstm_dw.pth")
elif crnn_type == "full_lstm":
    nh = 256
    LSTMFLAG = True
    crnn_model_path = os.path.join(father_path,"models/ocr-lstm.pth")
# crnn_model_path = os.path.join(father_path,"models/ocr-lstm.pth")

# from crnn.keys import  alphabet
from crnn.keys import  alphabetChinese as alphabet


#angle_class
lable_map_dict  =  { 0 : "hengdao",  1:"hengzhen",  2:"shudao",  3:"shuzhen"}
rotae_map_dict  =   {"hengdao": 180 , "hengzhen": 0 , "shudao": 180 , "shuzhen": 0 }
angle_type  = "shufflenetv2_05"
# angle_type  = "resnet18"
angle_model_path  =  os.path.join(father_path,"models/{}.pth".format(angle_type))

TIMEOUT=30