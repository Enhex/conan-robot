#include <iostream>
#include <Robot.h>

int main()
{
	auto pos = Robot::Mouse::GetPos();
	std::cout << "mouse position: " << pos.X << ',' << pos.Y << std::endl;
}
