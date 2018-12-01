//
// Created by yunle on 18-12-1.
//

#include <ros/ros.h>
#include <ctime>
#include <iostream>
#include <fstream>
#include <pcl/point_types.h>
#include <pcl/point_cloud.h>
#include <pcl/io/pcd_io.h>
using namespace std;
class Kitty2PCL {
private:
	ros::Publisher points_pub;

public:
	Kitty2PCL(){};
	~Kitty2PCL(){};

	void kitti2pcl(string &in_file, string &out_file) {
		// load pointCloud
		fstream input(in_file.c_str(), ios::in | ios::binary);
		if (!input.good()) {
			cerr << "Could not read file: " << in_file << endl;
			exit(EXIT_FAILURE);
		}
		input.seekg(0, ios::beg);  // 设置输入文件流的文件流指针位置   seekp()为输出文件流的文件流指针位置
		/**第二个参数指示偏移起始位置
		 * ios:beg  文件流的起始位置
		 * ios:cur  文件流的当前位置
		 * ios:end  文件流的结束位置
		 */
		pcl::PointCloud<pcl::PointXYZI>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZI>);
		int i;
		for (i = 0; input.good() && !input.eof(); i++) {
			pcl::PointXYZI point;
			input.read((char *) &point.x, 3 * sizeof(float));
			input.read((char *) &point.intensity, sizeof(float));
			cloud->push_back(point);
		}
		input.close();
		cout<<"Totally read "<<cloud->points.size()<<" points"<<endl;

		pcl::PCDWriter writer;
		writer.write<pcl::PointXYZI>(out_file,*cloud,false);

	}
};


int main(int argc,char** argv){
	string infile_name = "/home/yunle/temp/binFile/001250.bin";
	string outfile_name = "/home/yunle/temp/binFile/001250.pcd";

	Kitty2PCL app;
	app.kitti2pcl(infile_name,outfile_name);

	return 0;
}