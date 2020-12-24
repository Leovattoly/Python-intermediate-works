
#include <iostream> 
using namespace std;

struct BlueMount {
	int floor;
	int rooms;
	int single_room;
	int double_room;
	int king_room;
	int suite_room;
	float profit;

};

int main()
{
	struct BlueMount hotel[4];
	start:
	for (int i = 0; i < 4; ++i)
	{
		cout << "Enter the Number of floors in Hotel " << i + 1 << "\n";
		cin >> hotel[i].floor;
		if (hotel[i].floor > 0 && hotel[i].floor < 6)
		{
			for (int j = 0; j < hotel[i].floor; ++j)
			{
				cout << "\nEnter the Numer of total rooms in  " << j + 1 << "th floor\n: ";
				cin >> hotel[i].rooms;
				cout << "\nPlease enter the number of Single room: \n";
				cin >> hotel[i].single_room;
				cout << "\nPlease enter the number of Double room: \n";
				cin >> hotel[i].double_room;
				cout << "\nPlease enter the number of King room: \n";
				cin >> hotel[i].king_room;
				cout << "\nPlease enter the number of Suite room: \n";
				cin >> hotel[i].suite_room;
				if (hotel[i].rooms != (hotel[i].single_room + hotel[i].double_room + hotel[i].king_room + hotel[i].suite_room))
				{
					cout << "Incorrect room numbers ";
					goto start;
				}
				cout << "\nPlease enter the number of occupied Single room: \n";
				cin >> hotel[i].single_room;
				cout << "\nPlease enter the number of occupied Double room: \n";
				cin >> hotel[i].double_room;
				cout << "\nPlease enter the number of occupied King room: \n";
				cin >> hotel[i].king_room;
				cout << "\nPlease enter the number of  occupied Suite room: \n";
				cin >> hotel[i].suite_room;
				hotel[i].profit += hotel[i].single_room * 60 + hotel[i].double_room * 75 + hotel[i].king_room * 100 + hotel[i].suite_room * 150;
			}
		}
		else
		{
			cout << "Incorrect floor numbers ";
			goto start;
		}
		cout << "\nHotel " << i + 1 << " Total Income:" << hotel[i].profit;
	}

	return 0;
}
