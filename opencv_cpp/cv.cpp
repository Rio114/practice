#include<iostream>
#include <opencv2/opencv.hpp>
// #include <opencv/highgui.h>

int main() {
    cv::Mat img =  cv::imread("g2-6.jpg", -1);
    cv::Vec3b bgr = img.at<cv::Vec3b>(0, 0);

    unsigned int b = bgr[0];
    unsigned int g = bgr[1];
    unsigned int r = bgr[2];
    std::cout << b << " " << g << " " << r << std::endl;

    // cv::imshow("title", img);
    // cv::waitKey(0);
    // cv::cvtColor(img, gray, CV_BGR2GRAY);
    // cv::imwrite("gray.png", gray);

    return 0;
}