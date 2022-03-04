from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing import image
from django.core.files.storage import FileSystemStorage
from .models import Test
import tensorflow as tf
import numpy as np


class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
img_height, img_width=32,32
new_model = load_model("./models/img_classifier.h5")

def main(request):
    context = {    }
    return render(request, 'img_cnn/home.html', context)

def prediction(request):
    print(request)
    print(request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName

    img = image.load_img(testimage, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    predictions = new_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    res_class = class_names[np.argmax(score)]
    res_score = 100 * np.max(score)
    res = "{} with a {:.2f} percent confidence.".format(res_class, res_score)
    res = str(res)

    new_entity = Test(res_class, filePathName)
    new_entity.save()

    context={'filePathName':filePathName, 'result':res}
    return render(request, 'img_cnn/home.html', context)

def see_all(request):
    context = {
        'res': Test.objects.all(),
    }
    return render(request,'img_cnn/view_all.html',context) 
