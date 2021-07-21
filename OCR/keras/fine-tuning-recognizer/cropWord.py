#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2


class CropWord:
    def __init__(self, mainFolder, datasetFolder, imgName, imgFormat):
        self.mainFolder = mainFolder
        self.datasetFolder = datasetFolder
        self.imgName = imgName
        self.imgFormat = imgFormat
        self.npoints = 4
        self.img = cv2.imread(f'{mainFolder}/{imgName}.{imgFormat}', cv2.IMREAD_COLOR)
        self.pts = []
        self.final_image = []
        self.boxPoints = []
        self.word = ''
        self.cropedFilename = ''
        self.label = []
        self.labels = []

    def callMe(self):
        self.pts, self.final_image = self.get_points(self.img)
        return self.labels

    def get_points(self, image):
        # Set up data to send to mouse handler
        data = {}
        data['image'] = image.copy()
        data['lines'] = []

        # Set the callback function for any mouse event
        cv2.imshow("Image", image)
        cv2.setMouseCallback("Image", self.mouse_handler, data)
        cv2.waitKey(0)

        points = data['lines']

        return points, data['image']

    def cropAndSave(self):
        '''
        Crop word from the image
        We consider (0,0) as top left corner of image called im with left-to-right as x direction
        and top-to-bottom as y direction. and we have (x1,y1) as the top-left vertex and (x2,y2)
        as the bottom-right vertex of a rectangle region within that image, then:
        roi = image[y1 : y2, x1 : x2]
        '''
        # print(f'({min(self.boxPoints)[0]}, {min(self.boxPoints)[1]}), ({max(self.boxPoints)[0]}, {max(self.boxPoints)[1]})')
        # img_crop = self.img[min(self.boxPoints)[1] : max(self.boxPoints)[1], min(self.boxPoints)[0] : max(self.boxPoints)[0]]
        img_crop = self.img[self.boxPoints[0][1] : self.boxPoints[2][1], self.boxPoints[0][0] : self.boxPoints[2][0]]
        
        # Save cropped image 
        cv2.imwrite(f'{self.mainFolder}/{self.datasetFolder}/{self.imgName}_{self.word}.{self.imgFormat}', img_crop)

    def mouse_handler(self, event, x, y, flags, data):
        if event == cv2.EVENT_LBUTTONDOWN:
            data['lines'].append((x, y))
            
            print('Point {}: {}'.format(len(data['lines']), data['lines'][-1]))   

            if len(data['lines']) >= 2:
                cv2.line(
                    data['image'],
                    data['lines'][len(data['lines']) - 2],
                    data['lines'][len(data['lines']) - 1],
                    (0, 0, 255),
                    1)
                cv2.imshow("Image", data['image'])

            if len(data['lines']) == self.npoints:
                # print("Next word...")
                cv2.line(
                    data['image'],
                    data['lines'][0],
                    data['lines'][len(data['lines']) - 1],
                    (0, 0, 255),
                    1)
                cv2.imshow("Image", data['image'])

                self.boxPoints = data['lines']
                # print("Box points:")
                # print(self.boxPoints)

            if len(data['lines']) > 3:
                data['lines'] = []                

        elif event == cv2.EVENT_MOUSEMOVE and len(data['lines']) >= 1:
            # print('Position: ({}, {})'.format(x, y))
            image = data['image'].copy()

            if len(data['lines']) < self.npoints:
                # this is just for a line visualization
                cv2.line(image, data['lines'][len(data['lines']) - 1], (x, y), (0, 255, 0), 1)

            cv2.imshow("Image", image)

        elif event == cv2.EVENT_RBUTTONDOWN:
            self.word = input('Palavra: ') 

            self.label.extend([
                f'{self.mainFolder}/{self.datasetFolder}/{self.imgName}_{self.word}.{self.imgFormat}',
                self.boxPoints,
                self.word
            ])
            self.labels.append(tuple(self.label))
            # print(self.labels)

            self.cropAndSave()

            self.boxPoints, self.label = [], []            

            # file = open(f'{self.mainFolder}/{self.imgName}.txt', 'w')
            # file.write("{}".format(self.box))
            # file.close()
