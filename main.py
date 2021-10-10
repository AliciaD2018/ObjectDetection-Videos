import time

import cv2
import numpy as np
import threading
from multiprocessing import Process
import os

path = 'C:/Users/alicia/Documents/Semestre II 2021/Principios de Sistemas Operativos/yoloImage/'

def detectar(video):
    start_time = time.time()
    cap = cv2.VideoCapture(video)
    whT = 320
    confThreshold = 0.5
    nmsThreshold = 0.3

    classesFile = 'obj.names'
    classNames = []

    with open(classesFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    modelConfiguration = 'config/yolov3.cfg'
    modelWeights = 'config/yolov3.weights'

    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    lista = []
    def findObjects(outputs, img):
        hT, wT, cT = img.shape
        bbox = []
        classIds = []
        confs = []
        tiempo = 0
        nombre = ""
        for output in outputs:
            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]

                if confidence > confThreshold:
                    w, h = int(det[2] * wT), int(det[3] * hT)
                    x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))

        indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)
        for i in indices:
            i = i[0]
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

            time_milli = cap.get(cv2.CAP_PROP_POS_MSEC)
            if classNames[classIds[i]] != "":
                tiempo = round(time_milli / 1000)
                if tiempo not in lista:
                    nombre = classNames[classIds[i]]
                    cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%',
                                (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

        return tiempo, nombre

    aux = 1
    contador = 0
    while True:
        success, img = cap.read()
        if aux % 2 != 0:
            if (success == True):
                contador+=1
                blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
                net.setInput(blob)

                layerNames = net.getLayerNames()
                outputNames = [layerNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
                outputs = net.forward(outputNames)

                tiempo, nombre = findObjects(outputs, img)
                if nombre != "":
                    if tiempo not in lista:
                        lista.append(tiempo)
                        cv2.imwrite(path + str(nombre) + str(tiempo) + '.png', img)

                cv2.imshow('Image', img)
                cv2.waitKey(1)
            else:
                print("--- %s seconds ---" % (time.time() - start_time))
                break
            aux+=1
        else:
            aux+=1

if __name__ == '__main__':
    cores=os.cpu_count()
    print('Tengo ',cores, ' cores')
    proceso=Process(target=detectar, args=('3.mp4',))
    proceso2=Process(target=detectar,args=('Caceria.mp4',))
    proceso.start()
    proceso2.start()
    proceso.join()

    #thread = threading.Thread(target=detectar, args=('3.mp4',))
    #thread.start()

#------------------------------------------------------------------------
