#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2


class BoxMaker:
    def __init__(self, folder, imgName, imgFormat):
        self.folder = folder
        self.imgName = imgName
        self.npoints = 4
        self.img = cv2.imread(f'{folder}/{imgName}.{imgFormat}', cv2.IMREAD_COLOR)
        self.pts = []
        self.final_image = []
        self.content = [] 
        self.box = []

    def callMe(self):
        self.pts, self.final_image = self.get_points(self.img)
        # print(self.pts)
        return self.box

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


    def mouse_handler(self, event, x, y, flags, data):
        if event == cv2.EVENT_LBUTTONDOWN:
            data['lines'].append((x, y))

            # print('Add point: ', data['lines'])
            print('Point {}: {}'.format(len(data['lines']), data['lines'][-1]))   

            if len(data['lines']) >= 2:
                cv2.line(
                    data['image'],
                    data['lines'][len(data['lines']) - 2],
                    data['lines'][len(data['lines']) - 1],
                    (0, 0, 255),
                    1)
                cv2.imshow("Image", data['image'])
            # else:
            #     cv2.circle(data['image'], (x, y), 3, (0, 0, 255), 5)
            #     cv2.imshow("Image", data['image'])

            if len(data['lines']) == self.npoints:
                print("Next letter...")
                cv2.line(
                    data['image'],
                    data['lines'][0],
                    data['lines'][len(data['lines']) - 1],
                    (0, 0, 255),
                    1)
                cv2.imshow("Image", data['image'])

                self.content.append(data['lines'])
                # print("CONTENT:")
                # print(self.content)       

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
            self.box.append(self.content)
            # print("BOX:")
            # print(self.box)
            self.content = []

            file = open(f'{self.folder}/{self.imgName}.txt', 'w')
            file.write("{}".format(self.box))
            file.close()
